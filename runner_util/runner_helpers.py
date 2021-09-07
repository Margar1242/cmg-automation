import json
import os
import shutil
import smtplib
import subprocess
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import os.path
from os import path

import requests

from runner_util.generate_html_report import GenerateHTMLReport
from helpers.helpers import read_file, get_platform_name, get_sheet_link
from runner_util.argument_parser import ArgParser
from constants.general_constants import *
from constants.runner_constants import *
from runner_util.serve_results import serve_results


def create_bash_command(args):
    bash_command = f"pytest -s --verbose --durations=0 " \
                   "--allure-link-pattern=test_case:link&range={} --allure-link-pattern=issue:link&range={}"
    platform_name, slash = get_platform_name()
    if args.page is not None:
        for page in args.page:
            bash_command += f" tests{slash}{page}_page_test.py"
    else:
        bash_command += f" tests{slash}"
    if args.thread_count is not None:
        bash_command += f" -n {args.thread_count}"
    if args.group:
        bash_command += f' -m {args.group}'
    if args.case:
        bash_command += f' -k {args.case}'
    return bash_command


def send_slack_report(args, passed, failed, skipped, error, browser, platform, duration, build_url, environment, sheet):
    color = Color.FAIL.value if failed > 0 or error > 0 else Color.PASS.value
    emoji = Emoji.THUMB_DOWN.value if failed > 0 or error > 0 else Emoji.THUMB_UP.value
    total = passed + failed + skipped + error
    now = datetime.now().strftime(TIME_FORMAT)
    report = Template(read_file(Templates.SLACK_TEMPLATE.value)).substitute(BROWSER=browser, DATE=now, EMOJI=emoji,
                                                                            COLOR=color, PLATFORM=platform,
                                                                            PASSED=passed, FAILED=failed,
                                                                            SKIPPED=skipped, ERROR=error, TOTAL=total,
                                                                            DURATION=duration, BUILD_URL=build_url,
                                                                            ENVIRONMENT=environment, SHEET=sheet)
    json_params_encoded = json.dumps(json.loads(report))
    requests.post(url=args.slack_hook, data=json_params_encoded, headers={CONTENT_TYPE: APPLICATION_JSON})


def send_email_report(args, passed, fail, skip, error, browser, platform, duration, build_url):
    status = Statuses.FAIL.value.upper() if fail > 0 or error > 0 else Statuses.PASS.value.upper()
    status_color = Color.RED.value if status == Statuses.FAIL.value.upper() else Color.GREEN.value
    now = datetime.now()
    total = passed + fail + skip + error
    msg = MIMEMultipart(ALTERNATIVE)
    to = args.to_email
    me = args.from_email
    msg[
        SUBJECT] = f"Test Automation Report | {passed}/{total} | {browser.upper()} |{now.strftime(TIME_FORMAT)}"
    msg['From'] = me
    msg['To'] = ", ".join(to)
    html = read_file(Templates.EMAIL_TEMPLATE.value)
    html = Template(html).substitute(PLATFORM=platform, ST_COLOR=status_color,
                                     STATUS=status, BROWSER=browser.upper(), FAILED=fail, PASSED=passed,
                                     SKIPPED=skip, ERROR=error, TOTAL=total, ENVIRONMENT=args.env,
                                     URL=args.env, DURATION=duration)
    part2 = MIMEText(html, "html")
    msg.attach(part2)
    s = smtplib.SMTP(args.smtp_host, args.smtp_port)
    s.starttls()
    s.login(me, args.password)
    s.sendmail(me, to, msg.as_string())


def run_command(argument: str):
    arguments = ArgParser().get_args()
    bash_command = create_bash_command(arguments)
    platform_name, slash = get_platform_name()
    if argument in arguments.browser:
        os.environ[BROWSER] = argument
        os.environ[TYPE] = arguments.type[0]
    if argument in arguments.type:
        os.environ[TYPE] = argument
        os.environ[BROWSER] = arguments.browser[0]
    bash_command += f' --alluredir=allure_results_{argument} --json-report --json-report-summary ' \
                    f'--json-report-file={argument}_report.json'
    subprocess.call(bash_command.split(' '))
    shell = False if platform_name != 'windows' else True
    make_dir = 'mkdir' if platform_name != 'windows' else 'md'
    copy = 'cp -r' if platform_name != 'windows' else 'xcopy /y /e /h'
    remove = 'rm -rf' if platform_name != 'windows' else 'rmdir /s /q'
    remove_file = 'rm -rf' if platform_name != 'windows' else 'del /f /q /s'
    move = 'mv' if platform_name != 'windows' else 'move /y'
    if not path.exists(f'reports'):
        subprocess.call(f"{make_dir} reports".split(' '), shell=shell)
    if path.exists(f'reports{slash}allure-reports_for_{argument}'):
        subprocess.call(
            f"{copy} reports{slash}allure-reports_for_{argument}{slash}history allure_results_{argument}".split(' '),
            shell=shell)
        subprocess.call(f"{remove} reports{slash}allure-reports_for_{argument}".split(' '), shell=shell)
    subprocess.call(f"allure generate allure_results_{argument} --clean -o allure-reports_for_{argument}".split(' '),
                    shell=shell)
    subprocess.call(f"{move} allure-reports_for_{argument} reports".split(' '), shell=shell)
    subprocess.call(f"{move} {argument}_report.json reports".split(' '), shell=shell)
    subprocess.call(f"{remove} allure_results_{argument}".split(' '), shell=shell)
    subprocess.call(f"{remove_file} output.json pytest_html_report.html".split(' '), shell=shell)
    if path.exists('archive'):
        subprocess.call(f"{remove} archive".split(' '), shell=shell)


def generate_device_config_file(args):
    automation = Automation.ANDROID.value if args.platform == Platforms.ANDROID.value else Automation.IOS.value
    mobile_browser = Browsers.CHROME.value if args.platform == Platforms.ANDROID.value else Browsers.SAFARI.value
    config = {
        Configs.PLATFORM_NAME.value: args.platform,
        Configs.PLATFORM_VERSION.value: args.deviceOs,
        Configs.AUTOMATION_NAME.value: automation,
        Configs.BROWSER.value: mobile_browser,
        Configs.DEVICE.value: args.device
    }
    with open(Files.DEVICE_CONFIG.value, 'w') as json_file:
        json.dump(config, json_file)


def generate_reports(arguments, file):
    generate_report = GenerateHTMLReport()
    generate_report.append_title(arguments.browser)
    browsers = ['chrome', 'safari', 'firefox']
    platform_name, slash = get_platform_name()
    for browser in browsers:
        if path.exists(f'reports{slash}{browser}_report.json'):
            with open(f'reports{slash}{browser}_report.json') as json_report:
                data = json.load(json_report)
                duration = f"{round(data[DURATION])} seconds"
                platform = data[ENVIRONMENT][PLATFORM]
                summary = data[SUMMARY]
                passed = summary[Statuses.PASS.value] if Statuses.PASS.value in summary else 0
                failed = summary[Statuses.FAIL.value] if Statuses.FAIL.value in summary else 0
                error = summary[Statuses.ERROR.value] if Statuses.ERROR.value in summary else 0
                skipped = summary[Statuses.SKIP.value] if Statuses.SKIP.value in summary else 0
            generate_report.append(browser, platform, duration, passed, failed, skipped, error)
            if arguments.send_slack and browser in arguments.browser:
                sheet_url = '---'
                if arguments.update_sheet == 'yes':
                    sheet_url = f'<{get_sheet_link(file)}|*Google Spreadsheet Link*>'
                send_slack_report(arguments, passed, failed, skipped, error,
                                  browser.capitalize(), platform, duration, arguments.build_url, arguments.env, sheet_url)
            if arguments.to_email is not None and browser in arguments.browser:
                send_email_report(arguments, passed, failed, skipped, error,
                                  browser, platform, duration, arguments.build_url)
    generate_report.generate()
    if path.exists(f'assets') and not path.exists(f'reports{slash}assets'):
        shutil.copytree('assets', f'reports{slash}assets')
    if arguments.results == "show":
        serve_results()
