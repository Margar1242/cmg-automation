import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BrowserActions:

    @staticmethod
    @allure.step("Switch to {1} iframe")
    def switch_to_iframe(driver, locator, time_out=30):
        try:
            return WebDriverWait(driver=driver, timeout=time_out, poll_frequency=0.3).until(
                ec.frame_to_be_available_and_switch_to_it(locator))
        except TimeoutException:
            raise TimeoutException(f"The {locator} element is not available after {time_out} seconds of wait")
