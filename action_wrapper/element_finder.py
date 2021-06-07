import time

import allure
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.remote.webelement import WebElement

from action_wrapper.move_actions import MoveActions
from action_wrapper.wait_actions import WaitActions


class ElementFinder:

    @staticmethod
    @allure.step("Find {1} element")
    def find_element(driver, locator, repeat=3, timeout=20) -> WebElement:
        is_stale = True
        element = None
        repeat_count = 0
        while is_stale and repeat_count < repeat:
            try:
                repeat_count += 1
                WaitActions.wait_until_element_is_visible(driver, locator, time_out=timeout)
                MoveActions.move_to_element_located(driver, locator)
                element = driver.find_element(*locator)
                is_stale = False
            except (StaleElementReferenceException, ElementNotInteractableException):
                # Firefox case
                time.sleep(0.3)
        return element

    @staticmethod
    def find_elements_by_css_selector(locator, css_selector, repeat=3):
        is_stale = True
        elements = None
        repeat_count = 0
        while is_stale and repeat_count < repeat:
            try:
                repeat_count += 1
                elements = locator.find_elements_by_css_selector(css_selector)
                is_stale = False
            except (StaleElementReferenceException, ElementNotInteractableException):
                # Firefox case
                time.sleep(0.3)
        return elements

    @staticmethod
    def find_element_by_css_selector(locator, css_selector, repeat=3):
        is_stale = True
        element = None
        repeat_count = 0
        while is_stale and repeat_count < repeat:
            try:
                repeat_count += 1
                element = locator.find_element_by_css_selector(css_selector)
                is_stale = False
            except (StaleElementReferenceException, ElementNotInteractableException):
                # Firefox case
                time.sleep(0.3)
        return element
