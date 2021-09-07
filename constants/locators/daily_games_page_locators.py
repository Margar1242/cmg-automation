import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class DailyGamesPageLocators:
    HEADER = 'div > header[class*="none"]' if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value} \
        else 'main > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)
    DAILY_GAMES = (By.CSS_SELECTOR, f'{HEADER} .menu_unlocked a')
    SUBCATEGORY_BLOCK = (By.CLASS_NAME, 'block-subcategorytermnodes')
