import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class MobileGamePageLocators:
    HEADER = 'div > header[class*="none"]' if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value} \
        else 'main > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)
    # MG-1
    PLAY_BUTTON = (By.ID, 'playNowButton')
    TIMER = (By.ID, 'm-timer-div')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '.continue-link-new > a')
    GAME_CONTENT = (By.ID, 'openfl-content')
    IFRAME = (By.ID, 'html5game')

    # MG-2
    SORRY_MESSAGE = (By.CSS_SELECTOR, '.my-4 .no-flash-overlay-mobile > p')

    # MG-3
    SHOW_MORE_BUTTON = (By.CLASS_NAME, 'more-link')

    # MG-4
    SHOW_LESS_BUTTON = (By.CLASS_NAME, 'less-link')
    MORE_TEXT = (By.CSS_SELECTOR, '.details > p')
