from selenium.webdriver.common.by import By


class LogInPageLocators:
    # L-1
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
    USER_PAGE = (By.CLASS_NAME, 'my-page')

    # L-4
    FORGOT_PASSWORD = (By.CLASS_NAME, 'forgot-password')
