from enum import Enum

PLATFORM = 'Platform'
ENVIRONMENT = 'environment'
DURATION = 'duration'
SUMMARY = 'summary'
SUBJECT = 'Subject'
ALTERNATIVE = 'alternative'
TIME_FORMAT = '%d/%m/%Y %H:%M:%S'
CONTENT_TYPE = 'Content-type'
APPLICATION_JSON = 'application/json'


class Templates(Enum):
    EMAIL_TEMPLATE = 'templates/email_report.html'
    SLACK_TEMPLATE = 'templates/slack_report.json'


class Statuses(Enum):
    PASS = 'passed'
    FAIL = 'failed'
    SKIP = 'skipped'
    ERROR = 'error'


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    FAIL = '#e51c23'
    PASS = '#259b24'


class Platforms(Enum):
    ANDROID = 'Android'
    IOS = 'iOS'


class Configs(Enum):
    PLATFORM_NAME = 'platformName'
    PLATFORM_VERSION = 'platformVersion'
    AUTOMATION_NAME = 'automationName'
    BROWSER = 'browserName'
    DEVICE = 'deviceName'


class Automation(Enum):
    ANDROID = 'UIAutomator2'
    IOS = 'XCUITest'


class Emoji(Enum):
    THUMB_UP = ':thumbsup:'
    THUMB_DOWN = ':thumbsdown:'
