from selenium.webdriver.common.by import By


class AccountSettingsLocators:
    # AS-1
    ACCOUNT_SETTINGS_TITLE = (By.CSS_SELECTOR, "h1[class *= 'title']")

    # Premium: Billing and Plan (for subscribers only)
    SHOW_PROFILE = (By.CSS_SELECTOR, "span[class='text-right'] a")
    LOGIN_ID_TITLE = (By.CSS_SELECTOR, "#edit-loginid-read-group > div > h3")
    LOGIN_ID_DESCRIPTION = (By.CSS_SELECTOR, "div[class *= 'login_id_description']")
    USERS_LOGIN_ID = (By.CSS_SELECTOR, "#loginid-change-wrapper > strong")
    CHANGE_BUTTON_LOGIN_ID = (By.ID, "view-loginid-edit-form")
    PASSWORD_TITLE = (By.CSS_SELECTOR, "#edit-login-id-info--2 > div > h3")
    MASKED_PASSWORD = (By.ID, "password-change-wrapper")
    CHANGE_BUTTON_PASSWORD = (By.ID, "view-password-edit-form")
    WANT_PEOPLE_TO_FOLLOW_TITLE = (By.CSS_SELECTOR, "#edit-follow-me-info > div > label")
    WANT_PEOPLE_TO_FOLLOW_DESCRIPTION = (By.CSS_SELECTOR, "#edit-follow-me-info--description > p")
    LEARN_MORE_LINK = (By.CSS_SELECTOR, "#edit-follow-me-info--description > p > a")
    FIRST_RADIOBUTTON = (By.CSS_SELECTOR, "#edit-follow-me > div > div:nth-child(1) > label > span")
    SECOND_RADIOBUTTON = (By.CSS_SELECTOR, "#edit-follow-me > div > div:nth-child(2) > label > span")
    SAVE_BUTTON_FOR_RADIOBUTTONS = (By.ID, "edit-submit-follow")
    KEEP_ME_LOGGED_IN_TITLE = (By.CSS_SELECTOR, "#edit-remember-me-header > div > label")
    KEEPMELOGGEDIN_CHECKMARK = (By.CSS_SELECTOR, "span[class='checkmark']")
    KEEP_ME_LOGGED_IN_BUTTON_TEXT = (By.CSS_SELECTOR, "span[class='form-check-label']")
    SAVE_BUTTON_FOR_KEEPMELOGGEDIN = (By.ID, "edit-remember-me-follow")
    CHANGE_APPEARANCE_TEXT = (By.CSS_SELECTOR, "#edit-remember-me-footer > div > p")
    CUSTOMIZE_MY_PAGE_LINK = (By.CSS_SELECTOR, "#edit-remember-me-footer > div > p > a")

    # AS-3
    CURRENT_LOGIN_ID = (By.ID, "edit-new-login-id")
    SAVE_BUTTON_FOR_LOGIN_ID = (By.ID, "edit-submit-user-loginid")
    CANCEL_BUTTON_FOR_LOGIN_ID = (By.ID, "edit-loginid-edit-cancel")

    # AS-4
    LOGIN_ID_INPUT = (By.ID, "edit-new-login-id")

    # AS-6
    ERROR_MESSAGE_FOR_LOGIN = (By.CSS_SELECTOR, "div[class*='form'] span[class='error']")

    # AS-8
    CURRENT_PASSWORD_FIELD = (By.ID, "edit-password")
    NEW_PASSWORD_FIELD = (By.ID, "edit-new-password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "edit-confirm-password")
    SAVE_BUTTON_FOR_PASSWORD = (By.ID, "edit-password-submit")
    CANCEL_BUTTON_FOR_PASSWORD = (By.ID, "edit-password-cancel")

    # AS-9
    ERROR_MESSAGE_FOR_PASSWORD = (By.CSS_SELECTOR, "div[class='cmg-subscription-error'] span[class='error']")

    # AS-10
    ERROR_MESSAGE_AT_LEAST_5_CHARACTER = (By.CSS_SELECTOR, "div[class='cmg-subscription-error'] span[class='error']")

    # AS-11
    FOLLOW_BUTTON = (By.CSS_SELECTOR, "input[class*=' button following-confirm-access-btn']")

    # 15
    USERNAME_FROM_HEADER = (By.CSS_SELECTOR, "div[class='user-name text-left'] a")
    # for login
    USERNAME = (By.ID, 'edit-name')
    PASSWORD = (By.ID, 'edit-pass')
    LOGIN_BUTTON = (By.CLASS_NAME, 'login')
    SUBMIT_BUTTON = (By.ID, 'edit-submit')
    # logout
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'div[class="right-header-block col-2 col-lg-3 pr-0"] a[class="logout pt-2"]')

    # mobile specific
    MOBILE_BURGER_BUTTON = (By.CSS_SELECTOR, "button[class='navbar-toggler']")
    MOBILE_LOGOUT_BUTTON = (By.CSS_SELECTOR, 'div[class="mobile-menu-items"] a[class="logout pt-2"]')


class AccountSettingsPageStaticTexts:
    # AS-5
    CHANGED_LOGIN_ID = "aaa111aaa"

    # AS-1
    ACCOUNT_SETTINGS_EXPECTED_TITLE = "ACCOUNT SETTINGS"
    LOGIN_ID_EXPECTED_TITLE = "LOGIN ID"
    LOGIN_ID_EXPECTED_DESCRIPTION = "You use this to login, and nobody else can see it :"
    PASSWORD_EXPECTED_TITLE = "PASSWORD"
    WANT_PEOPLE_EXPECTED_TITLE = "WANT PEOPLE TO BE ABLE TO FOLLOW YOU?"
    WANT_PEOPLE_EXPECTED_DESCRIPTION = "When you follow someone on Coolmath Games, you’ll get a link to their " \
                                       "profile page to see the games they’re playing and the levels they’re " \
                                       "reaching Learn More."
    FIRST_RADIOBUTTON_EXPECTED_TEXT = "Sure, other players on Coolmath Games can follow me"
    SECOND_RADIOBUTTON_EXPECTED_TEXT = "Nope, don’t let anyone on Coolmath Games follow me"
    KEEP_ME_LOGGED_IN_EXPECTED_TITLE = "KEEP ME LOGGED IN"
    KEEP_ME_LOGGED_CHECKMARK_EXPECTED_TEXT = "Keep me logged in on this computer"
    CHANGE_APPEARANCE_TEXT = "To change the appearance of your profile, go to Customize My Page"

    USERNAME_1 = "testrafik"
    PASSWORD_1 = "testrafik"

    USERNAME_2 = "testroland"
    PASSWORD_2 = "testroland"
