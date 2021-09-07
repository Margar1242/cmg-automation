import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class MobileSpecificLocators:
    HEADER = 'div > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)

    # MOB-1
    SEARCH_BAR = (By.CSS_SELECTOR, f'{HEADER} .menu-search-bar')
    AZ_GAMES = (By.CSS_SELECTOR, f'{HEADER} .menu_allgames a')
    STRATEGY = (By.CSS_SELECTOR, f'{HEADER} .menu_strategy a')
    NUMBERS = (By.CSS_SELECTOR, f'{HEADER} .menu_numbers a')
    TRIVIA = (By.CSS_SELECTOR, f'{HEADER} .menu_trivia a')
    SKILL = (By.CSS_SELECTOR, f'{HEADER} .menu_skill a')
    LOGIC = (By.CSS_SELECTOR, f'{HEADER} .menu_logic a')
    PLAYLISTS = (By.CSS_SELECTOR, f'{HEADER} .menu_playlists a')
    DAILY_GAMES = (By.CSS_SELECTOR, f'{HEADER} .menu_unlocked a')
    MORE = (By.CSS_SELECTOR, f'{HEADER} .menu__item')
    SIGNUP_BUTTON = (By.CSS_SELECTOR, f'{HEADER} .free-account')
    LOGIN_BUTTON = (By.CSS_SELECTOR, f'{HEADER} .login')

    # MOB-2
    CLASSIC = (By.CSS_SELECTOR, f'{HEADER} .menu_classic')
    PUZZLES = (By.CSS_SELECTOR, f'{HEADER} .menu_puzzles')
    GEOGRAPHY = (By.CSS_SELECTOR, f'{HEADER} .menu_geography')
    WORD_GAMES = (By.CSS_SELECTOR, f'{HEADER} .menu_word')
    MEMORY = (By.CSS_SELECTOR, f'{HEADER} .menu_memory')
    SCIENCE = (By.CSS_SELECTOR, f'{HEADER} .menu_science')
    MORE_BUTTON = (By.CSS_SELECTOR, f'{HEADER} .menu_more')

    # MOB-4
    USERNAME_INPUT = (By.ID, 'edit-name')
    PASSWORD = (By.ID, 'edit-pass')
    SUBMIT = (By.ID, 'edit-submit')
    DROPDOWN = (By.ID, 'dropdownMenu-0')
    DROPDOWN_ITEMS = (By.CLASS_NAME, 'dropdown-menu')
    USER_PROFILE_BUTTON = (By.CSS_SELECTOR, f'{HEADER} .my-page')

    # MOB-5
    VIEW_ALL_BUTTON = (By.CSS_SELECTOR, '#tab1 .view-all-mobile')
    MY_GAMES = (By.ID, 'tab1-inner')

    MAIN_PAGE_GAMES = (By.CLASS_NAME, 'block-newcategoryhomefeatured')
    TOGGLE = (By.CLASS_NAME, 'navbar-toggler')
