import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class GlobalHeaderNavigationLocators:
    # GH-1
    HEADER = 'div > header[class*="none"]' if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value} \
        else 'main > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)
    LOGIN_BUTTON = (By.CSS_SELECTOR, f'{HEADER} .login')
    LOGIN_FORM = (By.ID, 'user-login-form',)
    TOGGLE = (By.CLASS_NAME, 'navbar-toggler')  # mobile

    # GH-2
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, f'{HEADER} .free-account')
    SIGN_UP_FORM = (By.ID, 'user-register-form')

    # GH-3
    NICKNAME = (By.ID, 'edit-name')
    PASSWORD = (By.ID, 'edit-pass')
    SUBMIT_BUTTON = (By.ID, 'edit-submit')
    AVATAR = (By.CSS_SELECTOR, f'{HEADER} #block-coolmath-branding')
    USERNAME = (By.CSS_SELECTOR, f'{HEADER} .user-name')
    PROGRESS_BAR = (By.CSS_SELECTOR, f'{HEADER} .progress')
    USER_PROFILE = (By.CSS_SELECTOR, f'{HEADER} .welcome-box')
    LOG_OUT = (By.CSS_SELECTOR, f'{HEADER} .logout')
    MAIN_PAGE_GAMES = (By.CLASS_NAME, 'img-fluid')

    # GH-4
    CLOSE_AD_POPUP = (By.CLASS_NAME, 'btn-close')
