from selenium.webdriver.common.by import By


class GamePageLocators:
    # GP-1
    TIMER = (By.ID, 'timer_div')
    GAME_LOADING_TEXT = (By.CLASS_NAME, 'loadingText')
    AD_CONTAINER = (By.ID, 'adcontainer')

    # GP-2
    CONTINUE_BUTTON = (By.CLASS_NAME, 'continue-link-yellow')

    # GP-3
    PROGRESS_BAR = (By.CLASS_NAME, 'game-xp-progress')
    FULL_SCREEN_BUTTON = (By.CLASS_NAME, 'requestfullscreen')

    # GP-4
    PLAYLISTS_BUTTON = (By.CLASS_NAME, 'mb-2')

    # GP-5, GP-6
    ALSO_LIKE_SECTION = (By.CLASS_NAME, 'view-display-id-carousel_game_detail')
    ALSO_LIKE_SECTION_GAMES = (By.CSS_SELECTOR, '.jcarousel:first-child ul:first-child')
    RIGHT_ARROW = (By.CLASS_NAME, 'jcarousel-control-next')
    LEFT_ARROW = (By.CLASS_NAME, 'jcarousel-control-prev')

    # GP-8
    LIKE_BUTTON = (By.CSS_SELECTOR, 'img[alt="Like"]')

    # GP-9
    LIKE_THIS_GAME = (By.CSS_SELECTOR, '#thumbsup > span:nth-child(2)')
    GAME_NAME_TITLE = (By.CSS_SELECTOR, '.pane-title:first-child')
    DISLIKE_BUTTON = (By.CSS_SELECTOR, 'img[alt="Dislike"]')
    GAME_IFRAME = (By.ID, 'html5game')
    INSTRUCTIONS = (By.CLASS_NAME, 'game-instructions')
    SKIP_ALL_AD_BUTTON = (By.CLASS_NAME, 'skip-ad-btn')
    TOP_PICKS_SECTION = (By.ID, 'block-views-block-top-picks-games-block-1')

    # GP-10
    GEAR_PROMO = (By.CSS_SELECTOR, '.cmg-gear-promo img')
    GO_AD_FREE_PROMO = (By.CSS_SELECTOR, '#monthly-subscription-plan > a > img')
    PROFILE_PROMO = (By.CLASS_NAME, 'profiles-promo')
    AZ_GAMES_SECTION = (By.CLASS_NAME, 'aside-link-title')
    AIMING_GAMES = (By.CSS_SELECTOR,
                    '.pane-queues-view-rightrail-games-promo > h2:first-child > a')
    AZ_GAME_LIST = (By.CSS_SELECTOR,
                    '.pane-queues-view-rightrail-games-promo')
    LEADERBOARD = (By.CSS_SELECTOR, '.leaderboard-promo > a > img')
