import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By

from utils.browser import make_chrome_browser


class RecipesbaseFunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:  # responsavel por criar o browser
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:  # Responsavel por matar o browser
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=6):
        time.sleep(seconds)


class RecipeHomePageFunctionalTest(RecipesbaseFunctionalTest):
    def test_recipe_home_page_without_recipes_error_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here', body.text)
