import argparse
import os
import re
import shutil
import json
from random import randint, choice
from platform import system
from constants.runner_constants import PLATFORM
from constants.general_constants import BROWSER


def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        return str(file.read())


def generate_random_email() -> str:
    return f"tester{randint(10, 99)}test{randint(1000, 9999)}@yopmail.com"


def remove_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass


def remove_files(files):
    for file in files:
        read_file(file)


def remove_directory(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def remove_directories(path):
    for directory in path:
        remove_directory(directory)


def remove_report_files():
    remove_directories(['reports', 'results_chrome', 'results_firefox', 'results_edge', 'results_safari'])


def dimensions(arg_value):
    pat = re.compile(r"^(\d{3,4})x(\d{3,4})$")
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError('Must be in the form NNNNxNNN, for example 1920x1080')
    return arg_value


def get_platform_name():
    platform_name = system().lower()
    slash = '/' if platform_name != 'windows' else '\\'
    return platform_name, slash


def generate_random_string():
    choices = (65, 90), (97, 122)
    return f'{"".join([chr(randint(*choice(choices))) for _ in range(3)])}{randint(1, 9999)}' \
           f'{"".join([chr(randint(*choice(choices))) for _ in range(4)])}{randint(1, 9999)}'


def define_key():
    browser = os.environ[BROWSER]
    platform = os.environ[PLATFORM]
    info = {'browser': browser.capitalize()}
    if platform != 'None':
        info[platform] = os.environ['mobile_os_version']
    return info


def get_spreadsheet_json_files(file):
    abs_path = os.path.dirname(os.path.abspath(file))
    return f'{abs_path}/configs/cmg_automation_auth.json', f'{abs_path}/configs/spreadsheet_config.json'


def load_spreadsheet_config_file(config_file):
    with open(config_file) as file:
        config = json.load(file)
    return config


def get_sheet_link(file):
    auth, config_file = get_spreadsheet_json_files(file)
    config = load_spreadsheet_config_file(config_file)
    url = 'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit#gid={sheet_id}'.format(**config)
    return url


def get_device_browser_version(driver, is_mobile=False):
    desired_capabilities = driver.desired_capabilities
    if is_mobile:
        browser_name = desired_capabilities['browserName']
        platform_version = desired_capabilities['platformVersion']
        browsers = driver.execute_script('return navigator.userAgent').lower().split(' ')
        os.environ['mobile_os_version'] = platform_version
        for item in browsers:
            if browser_name in item:
                return f"{item[item.index('/') + 1:]}"
    return desired_capabilities['browserVersion']
