from selenium.webdriver.common.by import By


class FooterLocators:

    # FT-1
    FOOTER = (By.CLASS_NAME, 'footer-menu')
    SUGGEST_GAME = (By.CSS_SELECTOR, '.pane-bean-footer-suggest-game a')
    SUBMIT_GAME = (By.CSS_SELECTOR, '.pane-bean-footer-submit-game a')
    PRIVACY_POLICY = (By.CSS_SELECTOR, '.pane-bean-footer-pivacy-policy .link-with-body-title a')
    COPYRIGHT = (By.CSS_SELECTOR, '.copyright-wrapper > p')
