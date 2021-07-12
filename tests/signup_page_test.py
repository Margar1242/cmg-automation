import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, RunModes
from pages.signup_page import SignupPage


@allure.feature("Signup Page")
@allure.story("Signup Page")
@pytest.mark.usefixtures("get_driver")
class TestLogInPage(TestCase):

    def setUp(self):
        self.signup_page: SignupPage = SignupPage(self.driver)
        self.signup_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify the structure of Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.signup
    @pytest.mark.web
    @pytest.mark.mobile
    def test_signup_page_structure(self):
        # SU-1
        expected_create_free_account_title = 'CREATE A FREE ACCOUNT'
        current_create_free_account_title = self.signup_page.get_free_account_title().upper()
        self.assertEqual(expected_create_free_account_title, current_create_free_account_title,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_create_free_account_title,
                                                                                    current_create_free_account_title,
                                                                                    'text'))
        expected_welcome_text = 'Welcome! Sign up to earn XP, level up, customize your page, create playlists, ' \
                                'and more!'
        current_welcome_text = self.signup_page.get_free_account_text()
        self.assertEqual(expected_welcome_text, current_welcome_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_welcome_text,
                                                                                    current_welcome_text,
                                                                                    'text'))
        expected_already_have_account_text = 'Already have an account? Log In.'
        current_already_have_account_text = self.signup_page.get_already_have_account_text()
        self.assertEqual(expected_already_have_account_text, current_already_have_account_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_already_have_account_text,
                                                                                    current_already_have_account_text,
                                                                                    'text'))
        login_button_expected_link = f'{self.signup_page.main_url()}/login'
        login_button_current_link = self.signup_page.get_login_button_link()
        self.assertEqual(login_button_expected_link, login_button_current_link,
                         msg=self.signup_page.exceptions['object_comparing'].format(login_button_expected_link,
                                                                                    login_button_current_link,
                                                                                    'urls'))
        login_info_expected_text = 'YOUR LOGIN INFO'
        login_info_current_text = self.signup_page.get_login_info_text()
        self.assertEqual(login_info_expected_text, login_info_current_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(login_info_expected_text,
                                                                                    login_info_current_text,
                                                                                    'text'))
        self.assertTrue(self.signup_page.login_id.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Login ID input'))

        expected_login_id_text = 'Create a Login ID. Other users won’t see it. Choose a name you’ll remember.'
        current_login_id_text = self.signup_page.get_login_id_text()
        self.assertEqual(expected_login_id_text, current_login_id_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_login_id_text,
                                                                                    current_login_id_text,
                                                                                    'text'))
        self.assertTrue(self.signup_page.password.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Password input'))
        self.assertTrue(self.signup_page.confirm_password.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Confirm password input'))
        self.assertTrue(self.signup_page.avatar_section.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Avatars section'))
        self.assertTrue(self.signup_page.themes.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Themes section'))
        self.assertTrue(self.signup_page.nickname_section.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Nickname section'))

        expected_nickname_section_text = 'This is the name that other users will see for you:'
        current_nickname_section_text = self.signup_page.get_nickname_section_text()
        self.assertEqual(expected_nickname_section_text, current_nickname_section_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_nickname_section_text,
                                                                                    current_nickname_section_text,
                                                                                    'text'))

        self.assertTrue(self.signup_page.suggested_username.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Suggested nickname'))
        self.assertTrue(self.signup_page.new_nickname_button.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('New nickname button'))

        expected_image = "premium.svg"
        current_image = self.signup_page.get_premium_membership_star()
        self.assertIn(expected_image, current_image,
                      msg=self.signup_page.exceptions['is_not'].format('Star icon', f'correct (expected: '
                                                                                    f'{expected_image}, current:'
                                                                                    f'{current_image})'))

        expected_custom_nickname_text = 'OR CREATE A CUSTOM NICKNAME'
        current_custom_nickname_text = self.signup_page.get_custom_nickname_text()
        self.assertEqual(expected_custom_nickname_text, current_custom_nickname_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_custom_nickname_text,
                                                                                    current_custom_nickname_text,
                                                                                    'text'))

        self.assertTrue(self.signup_page.create_custom_nickname.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Custom nickname field'))

        expected_premium_membership_text = 'Custom Nicknames require Premium Membership after you sign up. ' \
                                           'Membership includes Custom Nickname + all Premium Features!'
        current_premium_membership_text = self.signup_page.get_premium_membership_text()
        self.assertEqual(expected_premium_membership_text, current_premium_membership_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_premium_membership_text,
                                                                                    current_premium_membership_text,
                                                                                    'text'))
        self.assertTrue(self.signup_page.signup_button.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Signup button'))

    @allure.testcase('2')
    @allure.title('Verify premium avatar popup text of Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.signup
    @pytest.mark.web
    @pytest.mark.mobile
    def test_premium_avatar_popup_text(self):
        # SU-4
        self.signup_page.click_on_random_premium_avatars()
        self.assertTrue(self.signup_page.premium_avatar_popup.is_displayed(),
                        msg=self.signup_page.exceptions['not_displayed'].format('Premium avatar popup'))
        expected_popup_text = "Premium Avatars require Premium Membership after you sign up. You'll get this avatar " \
                              "plus all Premium Avatars & Themes!"
        current_popup_text = self.signup_page.get_popup_text()
        self.assertEqual(expected_popup_text, current_popup_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_popup_text,
                                                                                    current_popup_text,
                                                                                    'text'))

    @allure.testcase('3')
    @allure.title('Verify error message for duplicate ID of Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.signup
    @pytest.mark.web
    @pytest.mark.mobile
    def test_id_error_message(self):
        # SU-5
        self.signup_page.enter_not_valid_params()
        expected_error_text = 'Sorry, that Login ID is already taken. Please try another one.'
        current_error_text = self.signup_page.get_duplicate_id_error_message()
        self.assertEqual(expected_error_text, current_error_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_error_text,
                                                                                    current_error_text,
                                                                                    'text'))

    @allure.testcase('4')
    @allure.title('Verify error message for not matched password and confirm password fields and of Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.signup
    @pytest.mark.web
    @pytest.mark.mobile
    def test_error_message(self):
        # SU-6
        self.signup_page.enter_not_valid_params(incorrect_password=True)
        expected_error_text = "Passwords do not match"
        current_error_text = self.signup_page.get_not_matched_password_error_message()
        self.assertEqual(expected_error_text, current_error_text,
                         msg=self.signup_page.exceptions['object_comparing'].format(expected_error_text,
                                                                                    current_error_text,
                                                                                    'text'))

    @allure.testcase('5')
    @allure.title('Verify correct signup of Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.signup
    @pytest.mark.web
    @pytest.mark.mobile
    def test_correct_signup(self):
        # SU-7
        self.signup_page.click_new_nickname_button()
        username = self.signup_page.get_suggested_username()
        expected_url_part = f'{self.signup_page.main_url()}/profile/{username}'
        self.signup_page.enter_valid_params(username)
        current_url = self.signup_page.current_url()
        self.assertIn(expected_url_part, current_url,
                      msg=self.signup_page.exceptions['is_not'].format(expected_url_part, f'in {current_url}'))
        self.signup_page.logout()
        self.signup_page.get(self.signup_page.correct_url())

    @allure.testcase('6')
    @allure.title('Verify avatars section of Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.signup
    @pytest.mark.web
    @pytest.mark.mobile
    def test_avatars_section(self):
        # # SU-2
        expected_image = 'premium.svg'
        all_images, premium_images = self.signup_page.get_all_images()
        error_message = f'All avatar({len(all_images)}) and premium avatar ({len(premium_images)}) count are the same'
        self.assertNotEqual(len(all_images), len(premium_images), msg=error_message)
        for image in premium_images:
            self.assertIn(expected_image, image, msg=self.signup_page.exceptions['is_not'].format(expected_image,
                                                                                                  f'in {image}'))

        avatar_borders = self.signup_page.get_premium_image_border()
        expected_color = '#f7c649'
        for alt, color in avatar_borders.items():
            self.assertEqual(expected_color, color,
                             msg=self.signup_page.exceptions['object_comparing'].format(expected_color, color,
                                                                                        f'colors (avatar: {alt})'))

    @allure.testcase('7')
    @allure.title('Verify themes section of Signup Page')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.signup
    @pytest.mark.web
    @pytest.mark.mobile
    def test_themes_section(self):
        # SU-3
        all_themes, premium_themes = self.signup_page.get_all_images(section='theme', pseudo='before')
        expected_image = "data:image/svg+xml"
        error_message = f'All themes({len(all_themes)}) and premium themes ({len(premium_themes)}) count are the same'
        self.assertNotEqual(len(all_themes), len(premium_themes), msg=error_message)
        for image in premium_themes:
            self.assertIn(expected_image, image, msg=self.signup_page.exceptions['is_not'].format(expected_image,
                                                                                                  f'in {image}'))

        theme_borders = self.signup_page.get_premium_image_border(section="theme")
        expected_color = '#f7c649'
        for theme_name, color in theme_borders.items():
            self.assertEqual(expected_color, color,
                             msg=self.signup_page.exceptions['object_comparing'].format(expected_color, color,
                                                                                        f'colors (avatar: {theme_name})'
                                                                                        ))
