import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class HomePageLocator:
    # HP-1
    HEADER = 'div > header[class*="none"]' if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value} \
        else 'main > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)
    STRATEGY = (By.CSS_SELECTOR, f'{HEADER} .menu_strategy a')
    SKILL = (By.CSS_SELECTOR, f'{HEADER} .menu_skill a')
    NUMBERS = (By.CSS_SELECTOR, f'{HEADER} .menu_numbers a')
    LOGIC = (By.CSS_SELECTOR, f'{HEADER} .menu_logic a')
    TRIVIA = (By.CSS_SELECTOR, f'{HEADER} .menu_trivia a')
    MORE = (By.CSS_SELECTOR, f'{HEADER} .menu__item')
    PLAYLISTS = (By.CSS_SELECTOR, f'{HEADER} .menu_playlists a')
    RANDOM = (By.CSS_SELECTOR, f'{HEADER} .menu_random a')
    DAILY_GAMES = (By.CSS_SELECTOR, f'{HEADER} .menu_unlocked a')

    # HP-2
    TOP_TEN_GAMES_SECTION = (By.CLASS_NAME, 'top-ten-games')
    ALSO_LIKE_SECTION = (By.CLASS_NAME, 'view-display-id-carousel_game_detail')

    # HP-3
    ...

    TOGGLE = (By.CLASS_NAME, 'navbar-toggler')
