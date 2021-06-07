import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class WaitActions:
    @staticmethod
    @allure.step("Wait until {1} element to be visible")
    def wait_until_element_is_visible(driver, locator, time_out: int = 20):
        try:
            return WebDriverWait(driver=driver, timeout=time_out, poll_frequency=0.3,
                                 ignored_exceptions=(NoSuchElementException,
                                                     WebDriverException)).until(
                ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"The {locator} element is not located after {time_out} seconds of wait")

    @staticmethod
    @allure.step("Wait until {1} element to be invisible")
    def wait_until_element_is_invisible(driver, locator, time_out: int = 20):
        try:
            return WebDriverWait(driver=driver, timeout=time_out, poll_frequency=0.3).until(
                ec.invisibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"The {locator} element is not invisible after {time_out} seconds of wait")

    @staticmethod
    @allure.step("Wait until the page url contains {1}")
    def wait_until_url_contains(driver, url, time_out: int = 20):
        try:
            return WebDriverWait(driver=driver, timeout=time_out, poll_frequency=0.3).until(ec.url_contains(url))
        except TimeoutException:
            raise TimeoutException(f"After {time_out} seconds of wait the page url does not contain {url}")
