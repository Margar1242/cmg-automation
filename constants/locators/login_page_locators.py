import os
from selenium.webdriver.common.by import By
from constants.general_constants import TYPE, Types


class LogInPageLocators:
    # L-1
    HEADER = 'div > header[class*="none"]' if os.environ[TYPE] in {Types.MOBILE.value, Types.BS_MOBILE.value} \
        else 'main > header[class*="none"]'
    HEADER_LOCATOR = (By.CSS_SELECTOR, HEADER)
    LOGIN_TITLE = (By.CLASS_NAME, 'title')
    USERNAME = (By.ID, 'edit-name')
    PASSWORD = (By.ID, 'edit-pass')
    LOGIN_BUTTON = (By.CLASS_NAME, 'login')
    USER_SIGNUP = (By.CLASS_NAME, 'user-signup')
    SIGNUP_LINK = (By.CSS_SELECTOR, '.user-signup p:first-child strong a')

    # L-2
    ERR_MESSAGE = (By.CLASS_NAME, 'alert-dismissible')
    SUBMIT_BUTTON = (By.ID, 'edit-submit')

    # L-3
    GAME_IMAGE = (By.CLASS_NAME, 'img-fluid')

    # L-4
    FORGOT_PASSWORD = (By.CLASS_NAME, 'forgot-password')

    TOGGLE = (By.CLASS_NAME, 'navbar-toggler')
