import allure
from selenium.webdriver.remote.webdriver import WebDriver

from action_wrapper.element_actions import ElementActions
from action_wrapper.element_finder import ElementFinder
from constants.locators.footer_locators import FooterLocators
from pages.base_page import BasePage


class Footer(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page = ''

    def __getattr__(self, item):

        mapper = {
            'footer': FooterLocators.FOOTER,
        }

        return ElementFinder.find_element(self.driver, mapper[item])

    @allure.step("Get footer section all links for Footer")
    def get_footer_all_links(self):
        urls = {}
        elements = ElementFinder.find_element_from_element(self.footer, 'a', multiple=True)
        for element in elements:
            name = element.text
            value = ElementActions.get_attribute_from_element(element, 'href')
            urls[name] = value

        for item in [FooterLocators.SUGGEST_GAME, FooterLocators.SUBMIT_GAME, FooterLocators.PRIVACY_POLICY]:
            name = ElementActions.get_text(self.driver, item).upper()
            value = ElementActions.get_attribute(self.driver, item, 'href')
            urls[name] = value
        return urls

    @allure.step("Get copyright text for Footer")
    def get_copyright_text(self):
        return ElementActions.get_text(self.driver, FooterLocators.COPYRIGHT).replace('\n', '').replace('\t', '') \
            .strip()
