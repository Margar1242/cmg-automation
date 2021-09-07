from enum import Enum

BROWSER = 'BROWSER'
TYPE = 'TYPE'
URL = 'URL'
DIMENSIONS = 'DIMENSIONS'
THROUGHPUT = 'THROUGHPUT'
RUN_MODE = 'RUN_MODE'
HEADLESS = 'HEADLESS'
UPDATE_SPREADSHEET = 'No'


class Browsers(Enum):
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    SAFARI = 'safari'
    IE = 'ie'
    EDGE = 'edge'


class RunModes(Enum):
    SAVE_COOKIES = 'save_cookies'
    DELETE_COOKIES = 'delete_cookies'


class Types(Enum):
    DESKTOP = 'desktop'
    MOBILE = 'mobile'
    BS_DESKTOP = 'browser_stack_web'
    BS_MOBILE = 'browser_stack_mobile'


class Files(Enum):
    DEVICE_CONFIG = 'configs/device_config.json'
    BS_CONFIG = 'configs/bs_config.json'


class Urls(Enum):
    APPIUM_URL = 'http://localhost:4723/wd/hub'
    BS_URl = 'https://{}:{}@hub-cloud.browserstack.com/wd/hub'
