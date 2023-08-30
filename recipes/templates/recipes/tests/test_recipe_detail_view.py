from django.urls import resolve, reverse
from test_recipe_base import RecipeTestBase

from recipes import views


class RecipeDetailViewsTest(RecipeTestBase):

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertTrue(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        # teste para saber se os status code estão corretos
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 10000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipes(self):
        nedad_title = 'this is a detail page - It load one recipe'
        # Precisa de uma receita para este teste
        self.make_recipe(title=nedad_title)

        response = self.client.get(
            reverse('recipes:recipe',
                    kwargs={'id': 1}))
        # cliente abrindo a url
        content = response.content.decode('utf-8')
        # gerou uma resposta que gerou um conteudo que foi convertido string
        # chek if ONE_OR_MORE recipe exists
        self.assertIn(nedad_title, content)

    def test_recipe_detail_template_dont_load_recipes_not_published(self):
        """Testing recipe is published false dont show"""
        # Precisa de uma receita para este teste
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.id})
        )
        self.assertEqual(response.status_code, 404)
