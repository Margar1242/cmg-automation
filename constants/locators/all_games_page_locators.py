import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class AllGamesPageLocators:
    HEADER = 'div > header[class*="none"]' if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value} \
        else 'main > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)

    # AG-1
    AC = (By.CSS_SELECTOR, '#edit-title-1 > a')
    DG = (By.CSS_SELECTOR, '#edit-title-2 > a')
    HM = (By.CSS_SELECTOR, '#edit-title-3 > a')
    NR = (By.CSS_SELECTOR, '#edit-title-4 > a')
    SZ = (By.CSS_SELECTOR, '#edit-title-5 > a')

    # AG-2
    VIEW_ALL_GAMES_BUTTON = (By.CSS_SELECTOR, '#edit-title-all > a')
    GAME_URLS = (By.CLASS_NAME, 'view-all-games')
    GAME_TITLE = (By.CSS_SELECTOR, '.pane-title > span > span')

    # AG-3

    FLASH_ROBOT_IMAGE = (By.CSS_SELECTOR, '.flashIntroTxtImg > img')
    RELATED_GAMES = (By.CLASS_NAME, 'views-element-container')
    OFFERED_GAMES = (By.CSS_SELECTOR, '.views-element-container .views-row')
