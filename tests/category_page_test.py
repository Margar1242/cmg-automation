import os
from unittest import TestCase
import allure
import pytest

from constants.general_constants import RUN_MODE, RunModes
from pages.category_page import CategoryPage


@allure.feature("Category")
@allure.story("Category")
@pytest.mark.usefixtures("get_driver")
class TestCategoryPage(TestCase):

    def setUp(self):
        self.category_page: CategoryPage = CategoryPage(self.driver)
        self.category_page.get()

    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        # delete cookies before each test if should delete cookies
        if os.environ[RUN_MODE] == RunModes.DELETE_COOKIES.value:
            self.driver.delete_all_cookies()
            self.driver.refresh()
        yield

    @allure.testcase('1')
    @allure.title('Verify category page categories')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.category
    @pytest.mark.mobile
    @pytest.mark.web
    def test_category_page_categories(self):
        # CP-1
        categories = ['strategy', 'skill', 'numbers', 'logic', 'trivia', 'playlists', 'random', 'daily_games']
        expected_links = {'strategy': f'{self.category_page.main_url()}/1-strategy-games',
                          'skill': f'{self.category_page.main_url()}/1-skill-games',
                          'numbers': f'{self.category_page.main_url()}/1-number-games',
                          'logic': f'{self.category_page.main_url()}/1-logic-games',
                          'trivia': f'{self.category_page.main_url()}/trivia',
                          'playlists': f'{self.category_page.main_url()}/1-playlists',
                          'random': f'{self.category_page.main_url()}/random',
                          'daily_games': f'{self.category_page.main_url()}/1-daily-games'}
        for category in categories:
            if self.category_page.is_mobile and category == "random":
                continue
            self.category_page.click_on_category(category.upper())
            if category == 'random':
                self.category_page.get_also_like_section()
            current_url = self.category_page.current_url()
            expected_url = expected_links[category]
            if category == 'random':
                slash_index = current_url.rfind('/')
                question_mark_index = current_url.rfind('?')
                game_name = current_url[slash_index:question_mark_index]
                self.assertTrue(game_name, msg=self.category_page.exceptions['is_not'].
                                format(f'Game name', f'url ({current_url})'))
                self.assertTrue(current_url.endswith('random_true'), msg=self.category_page.exceptions['is_not'].
                                format(f'Current url ({current_url})', 'end with random_true'))
                continue
            self.assertEqual(current_url, expected_url,
                             msg=f'Expected ({expected_url}) and current {current_url} urls are different')

    # @allure.testcase('2')
    # @allure.title('Verify category page ads')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.category
    # @pytest.mark.mobile
    # @pytest.mark.web
    # def test_page_ads(self):
    #     # CP-2
    #     self.assertTrue(self.category_page.top_ad.is_displayed(),
    #                     msg=self.category_page.exceptions['not_displayed'].format('Top ad'))
    #     self.assertTrue(self.category_page.right_ad_1.is_displayed(),
    #                     msg=self.category_page.exceptions['not_displayed'].format('Right side first ad'))
    #     self.assertTrue(self.category_page.right_ad_2.is_displayed(),
    #                     msg=self.category_page.exceptions['not_displayed'].format('Right side second ad'))
    #     self.assertTrue(self.category_page.right_ad_3.is_displayed(),
    #                     msg=self.category_page.exceptions['not_displayed'].format('Right side third ad'))
    #     self.assertTrue(self.category_page.right_ad_4.is_displayed(),
    #                     msg=self.category_page.exceptions['not_displayed'].format('Right side fourth ad'))
    #     self.assertTrue(self.category_page.right_ad_5.is_displayed(),
    #                     msg=self.category_page.exceptions['not_displayed'].format('Right side fifth ad'))

    @allure.testcase('3')
    @allure.title('Verify category page MORE category')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.category
    @pytest.mark.mobile
    @pytest.mark.web
    def test_more_category(self):
        # CP-4
        expected_links = {
            'menu_classic': f'{self.category_page.main_url()}/1-classic-games',
            'menu_word': f'{self.category_page.main_url()}/1-word-games',
            'menu_puzzles': f'{self.category_page.main_url()}/0-jigsaw-puzzles',
            'menu_memory': f'{self.category_page.main_url()}/1-memory-games',
            'menu_geography': f'{self.category_page.main_url()}/1-geography-games',
            'menu_science': f'{self.category_page.main_url()}/1-science-games'
        }
        for category in expected_links:
            self.category_page.click_on_more_category(category)
            current_url = self.category_page.current_url()
            expected_url = expected_links[category]
            self.assertEqual(current_url, expected_url,
                             msg=self.category_page.exceptions['object_comparing'].
                             format(f'({expected_url})', f'({current_url})', 'url'))
