from selenium.webdriver.common.by import By


class BigScreenLocators:
    HEADER_LOCATOR = (By.CSS_SELECTOR, 'main > header[class*="none"]')
    LOADING_TEXT = (By.CLASS_NAME, 'loadingText')
    BIG_SCREEN_POPUP = (By.CLASS_NAME, 'big-screen-options-container')

    # BG-1
    BIG_SCREEN_BUTTON = (By.CLASS_NAME, 'requestfullscreen')
    CONTINUE_BUTTON = (By.CLASS_NAME, 'continue-link-yellow')

    # BG-2
    BIG_SCREEN_PROGRESS_BAR_CONTAINER = (By.CSS_SELECTOR, '.node__content > .game-xp-bar-immerse-button')
    PROGRESS_BAR = (By.CLASS_NAME, 'game-xp-progress')

    # BG-3
    BIG_SCREEN_POPUP_TEXT = (By.CSS_SELECTOR, '.truex_options_title > h1')
    X = (By.CLASS_NAME, 'btn-close')
    SPONSORED_VIDEO_BUTTON = (By.CLASS_NAME, 'truex_options_video')
    OR_TEXT = (By.CSS_SELECTOR, '.truex_options_OR_txt > h1')
    PREMIUM_ACCESS_BUTTON = (By.CLASS_NAME, 'truex_options_signup')
    RETURN_TO_REGULAR_MODE = (By.ID, 'cmg-big-screen-truex-promo-close')

    # BS-5
    BIG_SCREEN_IFRAME = (By.ID, 'big_screen_iframe')
    NOT_AVAILABLE_TEXT = (By.CSS_SELECTOR, '.pane-title > span > span')

    # BS-6
    POPUP = (By.ID, 'big-screen-truex-overlay')

    # BS-8
    POPUP_AD_COUNTDOWN = (By.ID, 'big-screen-truex-header-text')
    PLAY_BIG_SCREEN_NOW_BUTTON = (By.ID, 'truex-bigscreen-activate-id')

    # BS-9
    GAME_IFRAME = (By.ID, 'html5game')
    CANVAS = (By.CSS_SELECTOR, 'canvas')
    FULL_SCREEN_WINDOW = (By.CLASS_NAME, 'full-screen-window')

    # BS-10
    LOGIN = (By.CLASS_NAME, 'login')
    USERNAME = (By.ID, 'edit-name')
    PASSWORD = (By.ID, 'edit-pass')
    LOGIN_BUTTON = (By.ID, 'edit-submit')
    LOGOUT = (By.CLASS_NAME, 'logout')

    # BS-11
    EXIT_BIG_SCREEN = (By.CLASS_NAME, 'btn-fullscreen')

    # BS-12
    EMAIL_INPUT = (By.ID, 'edit-email')
    PASSWORD_INPUT = (By.ID, 'edit-pass')
    CC_NUMBER_IFRAME = (By.CSS_SELECTOR, '#card-element iframe')
    CC_NUMBER_INPUT = (By.CSS_SELECTOR, '.CardNumberField .InputElement')

    ZIP_CODE_IFRAME = (By.CSS_SELECTOR, '#address-zip-element iframe')
    ZIP_CODE_INPUT = (By.CSS_SELECTOR, '.InputContainer .InputElement')

    CARD_MM_YY_IFRAME = (By.CSS_SELECTOR, '#card-expiry-element iframe')
    CARD_MM_YY_INPUT = (By.CSS_SELECTOR, '.InputContainer .InputElement')

    ACCEPT_TERMS_BUTTON = (By.CLASS_NAME, 'tos-label')
    SUCCESS_TEXT = (By.CLASS_NAME, 'title')
    SUCCESS_PAGE_ELEMENT = (By.CLASS_NAME, 'big-screen-trial')
    PREMIUM_BUTTON = (By.ID, 'edit-card-submit')
