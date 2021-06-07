from selenium.webdriver.common.by import By


class HomePageLocator:
    # HP-1
    STRATEGY = (By.CSS_SELECTOR, '.menu_strategy a')
    SKILL = (By.CSS_SELECTOR, '.menu_skill a')
    NUMBERS = (By.CSS_SELECTOR, '.menu_numbers a')
    LOGIC = (By.CSS_SELECTOR, '.menu_logic a')
    TRIVIA = (By.CSS_SELECTOR, '.menu_trivia a')
    MORE = (By.CLASS_NAME, 'menu__item')
    PLAYLISTS = (By.CSS_SELECTOR, '.menu_playlists a')
    RANDOM = (By.CSS_SELECTOR, '.menu_random a')
    DAILY_GAMES = (By.CSS_SELECTOR, '.menu_unlocked a')

    # HP-2
    TOP_TEN_GAMES_SECTION = (By.CLASS_NAME, 'top-ten-games')
    ALSO_LIKE_SECTION = (By.CLASS_NAME, 'view-display-id-carousel_game_detail')

    # HP-3
    ...
