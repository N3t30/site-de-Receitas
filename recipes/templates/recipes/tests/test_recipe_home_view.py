from unittest.mock import patch

from django.urls import resolve, reverse
from test_recipe_base import RecipeTestBase

from recipes import views


class RecipeHomeViewsTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        # teste para saber se as funções estão corretas
        view = resolve(reverse('recipes:home'))
        self.assertTrue(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        # teste para saber se os templates estão corretos
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        # Precisa de uma receita para este teste
        self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        # cliente abrindo a url
        content = response.content.decode('utf-8')
        # gerou uma resposta que gerou um conteudo que foi convertido string
        response_context_recipes = response.context['recipes']
        # chek if ONE_OR_MORE recipe exists
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        """Testing recipe is published false dont show"""
        # Precisa de uma receita para este teste
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
        )

    def test_recipe_home_is_paginated(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)

        with patch('recipes.views.PER_PAGE', new=3):
            reponse = self.client.get(reverse('recipes:home'))
            recipes = reponse.context['recipes']
            paginator = recipes.paginator

        self.assertEqual(paginator.num_pages, 3)
        self.assertEqual(len(paginator.get_page(1)), 3)
        self.assertEqual(len(paginator.get_page(2)), 3)
        self.assertEqual(len(paginator.get_page(3)), 2)

    def test_invalid_page_query_users_page_one(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_data': {'username':
                                                       f'u{i}'}}
            self.make_recipe(**kwargs)

        with patch('recipes.views.PER_PAGE', new=3):
            response = self.client.get(reverse('recipes:home') + '?page=1A')
            self.assertEqual(
                response.context['recipes'].number, 1
            )

            response = self.client.get(reverse('recipes:home') + '?page=2')
            self.assertEqual(
                response.context['recipes'].number, 2
            )
