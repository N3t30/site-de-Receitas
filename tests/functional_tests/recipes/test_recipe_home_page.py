
from unittest.mock import patch

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import RecipesbaseFunctionalTest


# seleciona só os testes funcionais
@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipesbaseFunctionalTest):
    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_home_page_without_recipes_error_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here', body.text)

    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch
        # usuario abre a pagina
        self.browser.get(self.live_server_url)

        # Vê um campo de busca com o texto "search for a recipe"
        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Search for a recipe]'
        )

        # Clica neste input e digita o termo de busca
        # "Recipe title 1" para encontrar a receita com esse titulo
        search_input.send_keys(recipes[0].title)
        search_input.send_keys(Keys.ENTER)

        self.sleep(5)
