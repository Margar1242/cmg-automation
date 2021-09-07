import os
from unittest import TestCase
import allure
import pytest

from pages.premium_signup_page import PremiumSignupPage
from constants.premium_signup_constants import VARIANTS, ID_LIST
from constants.runner_constants import PLATFORM, Platforms


@allure.feature("Signup Page")
@allure.story("Signup Page")
@pytest.mark.usefixtures("get_driver")
class TestPremiumSignUpPage(TestCase):

    def setUp(self):
        self.signup_page: PremiumSignupPage = PremiumSignupPage(self.driver)
        self.signup_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        self.driver.delete_all_cookies()
        self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify the structure of Premium Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.premium_signup
    @pytest.mark.web
    @pytest.mark.mobile
    def test_premium_signup_page_structure(self):
        # PS-1
        self.signup_page.enter_username_password_nickname()

        expected_title_text = 'enable your premium avatar, theme, nickname & more'
        current_title_text = self.signup_page.get_title_text()
        self.assertEqual(expected_title_text, current_title_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_title_text,
                                                                                    current_title_text,
                                                                                    'texts'))
        self.assertTrue(self.signup_page.email_field.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('email field'))

        expected_payment_title_text = 'payment'
        current_payment_title_text = self.signup_page.get_payment_title_text()
        self.assertEqual(expected_payment_title_text, current_payment_title_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_payment_title_text,
                                                                                    current_payment_title_text,
                                                                                    'texts'))
        expected_membership_text = '$5.99/month membership. cancel anytime.'
        current_membership_text = self.signup_page.get_month_membership_text()
        self.assertEqual(expected_membership_text, current_membership_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_membership_text,
                                                                                    current_membership_text,
                                                                                    'texts'))
        self.assertTrue(self.signup_page.cc_number_field.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('CC number field'))

        self.assertTrue(self.signup_page.zip_field.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('ZIP code field'))

        expected_terms_of_use_text = 'please accept the terms of use'
        current_terms_of_use_text = self.signup_page.get_terms_of_use_text()
        self.assertEqual(expected_terms_of_use_text, current_terms_of_use_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_terms_of_use_text,
                                                                                    current_terms_of_use_text,
                                                                                    'texts'))
        expected_type = 'checkbox'
        current_type = self.signup_page.get_terms_of_use_checkbox()
        self.assertEqual(expected_type, current_type,
                         msg=self.signup_page.exceptions['is_not'].format(expected_type, current_type,
                                                                          'types for "Terms of Use"'))

        expected_terms_of_use_link = f'{self.signup_page.main_url()}/terms-use'
        current_terms_of_use_link = self.signup_page.get_terms_of_use_link()
        self.assertEqual(expected_terms_of_use_link, current_terms_of_use_link,
                         msg=self.signup_page.exceptions['is_not'].format(expected_terms_of_use_link,
                                                                          current_terms_of_use_link,
                                                                          'urls'))

        self.assertTrue(self.signup_page.premium_button.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Premium Button'))

    @allure.testcase('2')
    @allure.title('Verify premium access urls for Premium Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.premium_signup
    @pytest.mark.web
    @pytest.mark.mobile
    @pytest.mark.skipif(os.environ[PLATFORM] == Platforms.IOS.value, reason='IOS is not automated')
    def test_premium_access_urls(self):
        results = {f'PS-{num}': True for num in (2, 4, 6, 8, 9)}
        self.results.test_results.update(results)
        exception = False
        exception_message = ""

        for id_ in ID_LIST:
            for variant in VARIANTS:
                url = f'{self.signup_page.main_url()}/profile/premium-access/{id_}/{variant}'
                self.signup_page.get(url)

                # PS-2
                try:
                    if self.results.test_results['PS-2']:
                        self.signup_page.enter_incorrect_email()
                        self.assertTrue(self.signup_page.email_error.is_displayed(),
                                        msg=self.signup_page.exceptions['not_displayed'].format(f'Incorrect email '
                                                                                                f'error message '
                                                                                                f'({url})'))
                except AssertionError as e:
                    self.results.test_results['PS-2'] = False
                    exception_message += f"\n{str(e)}" if exception else str(e)
                    exception = True

                # PS-4
                try:
                    if self.results.test_results['PS-4']:
                        self.signup_page.enter_incorrect_card_number()
                        self.assertTrue(self.signup_page.cc_error.is_displayed(),
                                        msg=self.signup_page.exceptions['not_displayed'].format(
                                            f'Card number error message ({url})'))
                except AssertionError as e:
                    self.results.test_results['PS-4'] = False
                    exception_message += f"\n{str(e)}" if exception else str(e)
                    exception = True

                # PS-6
                try:
                    if self.results.test_results['PS-6']:
                        self.signup_page.enter_incorrect_zip_code()
                        self.signup_page.enter_correct_email()
                        self.assertTrue(self.signup_page.zip_error.is_displayed(),
                                        msg=self.signup_page.exceptions['not_displayed'].format(
                                            f'Zip code error message({url})'))
                except AssertionError as e:
                    self.results.test_results['PS-6'] = False
                    exception_message += f"\n{str(e)}" if exception else str(e)
                    exception = True

                # PS-8
                try:
                    if self.results.test_results['PS-8']:
                        self.signup_page.enter_valid_zip()
                        self.signup_page.click_on_premium_button()
                        self.assertTrue(self.signup_page.terms_error.is_displayed(),
                                        msg=self.signup_page.exceptions['not_displayed'].format(
                                            f'Terms error message({url})'))
                except AssertionError as e:
                    self.results.test_results['PS-8'] = False
                    exception_message += f"\n{str(e)}" if exception else str(e)
                    exception = True

                # PS-9
                try:
                    if self.results.test_results['PS-9']:
                        self.signup_page.click_on_terms_button()
                        expected_url = f'{self.signup_page.main_url()}/terms-use'
                        current_url = self.signup_page.current_url()
                        self.assertEqual(expected_url, current_url,
                                         msg=self.signup_page.exceptions['is_not'].format(expected_url, current_url,
                                                                                          f'urls (opened from {url})'))
                except AssertionError as e:
                    self.results.test_results['PS-9'] = False
                    exception_message += f"\n{str(e)}" if exception else str(e)
                    exception = True

        if exception:
            raise AssertionError(exception_message)

    @allure.testcase('3')
    @allure.title('Verify success registration for Premium Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.premium_signup
    @pytest.mark.web
    @pytest.mark.mobile
    def test_success_registration(self):
        # PS-10
        self.signup_page.enter_username_password_nickname()
        self.signup_page.enter_valid_params()

        expected_text = "YOU'VE GOT PREMIUM ACCESS! CHECK YOUR EMAIL FOR MORE DETAILS."
        current_text = self.signup_page.get_success_registration_text()
        self.assertEqual(expected_text, current_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_text, current_text,
                                                                                    'texts'))
