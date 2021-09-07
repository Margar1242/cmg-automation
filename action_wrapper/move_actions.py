import itertools
import os

import allure
from selenium.common.exceptions import TimeoutException, MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
from constants.runner_constants import PLATFORM, Platforms
from action_wrapper.wait_actions import WaitActions


class MoveActions:
    @staticmethod
    @allure.step("Move to {1} element to be visible")
    def move_to_element_located(driver, locator, time_out=30, repeat=3):
        element = None
        try:
            for _ in itertools.repeat(None, repeat):
                element = WaitActions.wait_until_element_is_visible(driver, locator)
                if os.environ[PLATFORM] in {Platforms.IOS.value, Platforms.ANDROID.value}:
                    raise MoveTargetOutOfBoundsException
                ActionChains(driver).move_to_element(element).perform()
        except TimeoutException:
            raise TimeoutException(f"The {locator} element is not found after {time_out} seconds of wait")
        except MoveTargetOutOfBoundsException:
            ActionChains(driver).move_to_element(element)
