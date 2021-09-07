import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, RunModes
from pages.general_test_cases_page import GeneralTestCasePage


@allure.feature("General Test Cases")
@allure.story("General Test Cases")
@pytest.mark.usefixtures("get_driver")
class TestGeneralTestCases(TestCase):

    def setUp(self):
        self.game_page: GeneralTestCasePage = GeneralTestCasePage(self.driver)
        self.game_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify ad container for General Test Cases')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.general_test_cases
    @pytest.mark.mobile
    @pytest.mark.web
    def test_pre_roll_loading(self):
        # GT-3
        if self.game_page.is_mobile:
            self.game_page.click_on_play_button()
        self.assertTrue(self.game_page.ad_container.is_displayed(),
                        msg=self.game_page.exceptions['not_displayed'].format('Ad container'))
