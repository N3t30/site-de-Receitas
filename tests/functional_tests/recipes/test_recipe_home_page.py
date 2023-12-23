
import pytest
from selenium.webdriver.common.by import By

from .base import RecipesbaseFunctionalTest


# seleciona só os testes funcionais
@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipesbaseFunctionalTest):
    def test_recipe_home_page_without_recipes_error_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here', body.text)
