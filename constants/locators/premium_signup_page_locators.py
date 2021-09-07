from selenium.webdriver.common.by import By


class PremiumSignupPageLocator:
    HEADER_LOCATOR = (By.CLASS_NAME, 'page__content')
    ALERT = (By.CLASS_NAME, 'alert')
    LOGIN_ID = (By.ID, 'edit-name')
    PASSWORD = (By.ID, 'edit-pass')
    CONFIRM_PASSWORD = (By.ID, 'edit-confirm-pass')
    NICKNAME = (By.ID, 'edit-custom-public-name')
    SIGNUP_BUTTON = (By.ID, 'edit-submit')

    # PS-1
    TITLE = (By.CLASS_NAME, 'title')
    EMAIL_FIELD = (By.ID, 'edit-email')
    PAYMENT_TITLE = (By.CSS_SELECTOR, '.payment-info > h3')
    MONTH_MEMBERSHIP_TEXT = (By.CSS_SELECTOR, '.payment-info > p:nth-child(3)')  # strong .... p
    CC_NUMBER_FIELD = (By.ID, 'card-element')
    ZIP_FIELD = (By.ID, 'address-zip-element')
    TERMS_TEXT = (By.CLASS_NAME, 'tos-label')
    TERMS_OF_USE_CHECKBOX = (By.CSS_SELECTOR, '.js-form-type-checkbox')
    TERMS_OF_USE_BUTTON = (By.CSS_SELECTOR, '.tos-label > a')
    GET_PREMIUM_BUTTON = (By.ID, 'edit-card-submit')

    # PS-2
    EMAIL_ERROR = (By.ID, 'edit-email-error')

    # PS-4
    CC_NUMBER_IFRAME = (By.CSS_SELECTOR, '#card-element iframe')
    CC_NUMBER_ERROR = (By.CLASS_NAME, 'cmg-subscription-error')
    CC_NUMBER_INPUT = (By.CSS_SELECTOR, '.CardNumberField .InputElement')

    # PS-6
    ZIP_CODE_IFRAME = (By.CSS_SELECTOR, '#address-zip-element iframe')
    ZIP_CODE_ERROR = (By.CLASS_NAME, 'cmg-subscription-error')
    ZIP_CODE_INPUT = (By.CSS_SELECTOR, '.InputContainer .InputElement')

    CARD_MM_YY_IFRAME = (By.CSS_SELECTOR, '#card-expiry-element iframe')
    CARD_MM_YY_INPUT = (By.CSS_SELECTOR, '.InputContainer .InputElement')
    CARD_MM_YY = (By.ID, 'card-expiry-element')

    # PS-8
    TERMS_ERROR = (By.ID, 'tos-error')

    # PS-10
    ACCEPT_TERMS_BUTTON = (By.CLASS_NAME, 'tos-label')
    SUCCESS_TEXT = (By.CLASS_NAME, 'title')
    CATEGORIES = (By.CLASS_NAME, 'navbar-container')
    HUD = (By.CLASS_NAME, 'user-hud')
