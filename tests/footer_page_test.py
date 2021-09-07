import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, RunModes
from constants.footer_urls import URLS
from pages.footer_page import Footer


@allure.feature("Footer")
@allure.story("Footer")
@pytest.mark.usefixtures("get_driver")
class TestFooter(TestCase):

    def setUp(self):
        self.footer: Footer = Footer(self.driver)
        self.footer.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify footer section')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.footer
    @pytest.mark.mobile
    @pytest.mark.web
    def test_footer_section(self):
        urls = self.footer.get_footer_all_links()

        for name, url in URLS.items():
            self.assertIn(name, urls, msg=self.footer.exceptions['is_not'].format(name, f'urls ({urls})'))
            if name == 'Instagram':
                continue
            if name == 'Facebook':
                if self.footer.is_mobile:
                    urls[name] = urls[name].replace('www', 'm')
                    URLS[name] = URLS[name].replace('www', 'm')
                self.assertEqual(urls[name], URLS[name],
                                 msg=self.footer.exceptions['object_comparing'].format(urls[name], URLS[name], 'texts'))
                continue
            if name == 'Twitter' and self.footer.is_mobile:
                urls[name] = urls[name].replace('twitter', 'mobile.twitter')
                URLS[name] = URLS[name].replace('twitter', 'mobile.twitter')
            self.footer.get(urls[name])
            expected_url = URLS[name]
            current_url = self.footer.current_url()
            self.assertEqual(expected_url, current_url,
                             msg=self.footer.exceptions['object_comparing'].format(expected_url, current_url, 'urls'))

        expected_copyright_text = '© 2021 Coolmath.com LLC. All Rights Reserved.'
        current_copyright_text = self.footer.get_copyright_text()
        self.assertEqual(expected_copyright_text, current_copyright_text,
                         msg=self.footer.exceptions['object_comparing'].format(expected_copyright_text,
                                                                               current_copyright_text,
                                                                               'texts'))
