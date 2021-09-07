import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class GeneralTestCaseLocators:
    HEADER = 'div > header[class*="none"]' if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value} \
        else 'main > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)

    # GT-3
    AD_CONTAINER = (By.CSS_SELECTOR, '#videoplayer iframe')

    PLAY_BUTTON = (By.CLASS_NAME, 'icon-circle')
