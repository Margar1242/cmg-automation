import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class SignupPageLocator:
    HEADER = 'div > header[class*="none"]' if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value} \
        else 'main > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)

    # SU-1
    CREATE_FREE_ACCOUNT_TITLE = (By.CSS_SELECTOR, '.col-md-12 > h1')
    WELCOME = (By.CSS_SELECTOR, '.col-md-12 > p:nth-child(1) > strong')
    ALREADY_HAVE_ACCOUNT = (By.CSS_SELECTOR, '.col-md-12 > p:nth-child(2)')
    LOGIN_BUTTON = (By.ID, 'cmg-xp-signup-page-login')
    LOGIN_INFO = (By.ID, 'your-login-info-label')
    LOGIN_ID = (By.ID, 'edit-name')
    LOGIN_ID_TEXT = (By.CSS_SELECTOR, '#edit-account > p:nth-child(2)')
    PASSWORD = (By.ID, 'edit-pass')
    CONFIRM_PASSWORD = (By.ID, 'edit-confirm-pass')
    PASSWORD_TEXT = (By.CSS_SELECTOR, '#edit-account > p:nth-child(4)')
    AVATAR_SECTION = (By.ID, 'edit-cmgavatarcontainer')
    THEMES = (By.ID, 'themes')
    NICKNAME_SECTION = (By.ID, 'edit-publicname-container')
    NICKNAME_TEXT = (By.CSS_SELECTOR, '#edit-publicname-container > p')
    SUGGESTED_USERNAME = (By.ID, 'edit-user-pubname-item')
    NEW_NICKNAME_BUTTON = (By.ID, 'edit-regen-public-name')
    CREATE_CUSTOM_NICKNAME = (By.ID, 'cmg-signup-custom-name-title')
    STAR_ICON = (By.CSS_SELECTOR, '#cmg-signup-custom-name-title::before')
    CUSTOM_NICKNAME = (By.ID, 'edit-custom-public-name')
    CUSTOM_NICKNAME_TEXT = (By.ID, 'edit-custom-public-name--description')
    SIGNUP_BUTTON = (By.ID, 'edit-submit')

    # SU-4
    PREMIUM_AVATAR_POPUP = (By.CLASS_NAME, 'popover-body')

    # SU-5
    DUPLICATE_ID_ERROR_TEXT = (By.CSS_SELECTOR, '.form-item--error-message:nth-child(2) > .error')

    # SU-6
    NOT_MATCHED_PASSWORD = (By.CSS_SELECTOR, '.form-item--error-message > .confirm-pass-error')

    # SU-7
    LOGOUT = (By.CSS_SELECTOR, f'{HEADER} .logout')
    CLOSE_POPUP = (By.CLASS_NAME, 'btn-close')
    MAIN_PAGE_LOGIN_BUTTON = (By.CSS_SELECTOR, f'{HEADER} .login')
    MAIN_PAGE_GAMES = (By.CLASS_NAME, 'views-element-container')

    ALERT_MESSAGE = (By.CSS_SELECTOR, '#showErrorProfileNickname .error')
    TOGGLE = (By.CLASS_NAME, 'navbar-toggler')

    VIEW_ALL_BUTTON = (By.CSS_SELECTOR, '.show-more:nth-child(2)')
