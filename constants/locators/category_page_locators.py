import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class CategoryPageLocators:
    # CP-1
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

    # CP-2
    TOP_AD = (By.ID, 'block-coolmath-adstop-homepage-728x90')
    RIGHT_AD_1 = (By.ID,
                  'google_ads_iframe_/45966600/pw/leaderboard_hp_0__container__')
    RIGHT_AD_2 = (By.ID, 'google_ads_iframe_/45966600/pw/medium_rectangle_hp_3__container__')
    RIGHT_AD_3 = (By.ID, 'google_ads_iframe_/45966600/pw/medium_rectangle_hp_1__container__')
    RIGHT_AD_4 = (By.ID, 'google_ads_iframe_/45966600/pw/medium_rectangle_hp_2__container__')
    RIGHT_AD_5 = (By.ID, 'google_ads_iframe_/45966600/pw/medium_rectangle_hp_4__container__')

    # CP-3
    ...

    # CP-5
    ALSO_LIKE_SECTION = (By.CLASS_NAME, 'view-display-id-carousel_game_detail')

    TOGGLE = (By.CLASS_NAME, 'navbar-toggler')
