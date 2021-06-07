from selenium.webdriver.common.by import By


class GlobalHeaderNavigationLocators:
    # GH-1
    LOGIN_BUTTON = (By.CLASS_NAME, 'login')
    LOGIN_FORM = (By.ID, 'user-login-form',)

    # GH-2
    SIGN_UP_BUTTON = (By.CLASS_NAME, 'free-account')
    SIGN_UP_FORM = (By.ID, 'user-register-form')

    # GH-3

    NICKNAME = (By.ID, 'edit-name')
    PASSWORD = (By.ID, 'edit-pass')
    SUBMIT_BUTTON = (By.ID, 'edit-submit')
    AVATAR = (By.ID, 'block-coolmath-branding')
    USERNAME = (By.CLASS_NAME, 'user-name')
    PROGRESS_BAR = (By.CLASS_NAME, 'progress')
    USER_PROFILE = (By.CLASS_NAME, 'welcome-box')
    LOG_OUT = (By.CLASS_NAME, 'logout')

    # GH-4
    CLOSE_AD_POPUP = (By.CLASS_NAME, 'btn-close')
