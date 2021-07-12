import argparse

from helpers.helpers import dimensions


class ArgParser:

    def __init__(self):
        self.args = None

    def parse_cmd_arguments(self):
        parser = argparse.ArgumentParser(
            description="Run Web UI tests",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('--env', type=str, default='https://stage.coolmathgames.com',
                            help='Set the environment in which tests will be run', )
        parser.add_argument('--type', nargs='+', default=['desktop'],
                            help='Set the type where tests should be run desktop or mobile',
                            choices=['desktop', 'mobile', 'browser_stack_web', 'browser_stack_mobile'])
        parser.add_argument('--page', '-p', nargs='+', help='run specific class tests',
                            choices=['home', 'login', 'game', 'global_header_navigation', 'mobile_game', 'trivia',
                                     'mobile_specific', 'category', 'signup'])
        parser.add_argument('--throughput', help='simulate internet connection speed')
        parser.add_argument('--group', type=str, default='', help='run specific group tests')
        parser.add_argument('--case', type=str, default='', help='Input page')
        parser.add_argument('--thread_count', '-t', default=None, help='run tests in parallel')
        parser.add_argument('--run_mode', type=str, help='run tests independent from each other',
                            choices=['save_cookies', 'delete_cookies'], default='save_cookies')
        parser.add_argument('--results', type=str, help='Show results after run',
                            choices=['show', 'cancel'], default='cancel')
        parser.add_argument('--browser', '-b', nargs='+',
                            help='specify the browser in which tests will be run, '
                                 'please note that you can specify multiple browsers',
                            default=['chrome'],
                            choices=['chrome', 'safari', 'firefox', 'edge'])
        parser.add_argument('--to_email', type=str, default=None, nargs='+',
                            help='to send email report to specified email address')
        parser.add_argument('--from_email', type=str, default='', help='specify sender email')
        parser.add_argument('--password', type=str, default='', help='specify sender password')
        parser.add_argument('--smtp_host', type=str, default='', help='specify SMTP host')
        parser.add_argument('--smtp_port', default='587', help='specify SMTP port')
        parser.add_argument('--send_slack', default=False)
        parser.add_argument('--slack_hook',
                            default='',
                            help='specify the Incoming Webhooks url')
        parser.add_argument('--headless', action='store_true')
        parser.add_argument('--dimensions', '-d', default='1920x1080', type=dimensions)
        parser.add_argument('--build_url', type=str, default=None,
                            help='URL for the Jenkins build that tests were run against')
        parser.add_argument('--platform', type=str, choices=['Android', 'iOS'],
                            help='specify platform for mobile')
        parser.add_argument('--deviceOs', type=str, help='specify device os for mobile')
        parser.add_argument('--device', type=str, help='specify device name for mobile')
        self.args = parser.parse_args()

    def get_args(self):
        if self.args is None:
            self.parse_cmd_arguments()
        return self.args
