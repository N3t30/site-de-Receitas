# from django.urls import reverse
# from test_recipe_base import RecipeTestBase


# class paginationTests(RecipeTestBase):
#     # vamos testar se estão sendo exibidas o numero correto de receitas por paginas. # noqa: E501
#     def test_pagination_max_9_recipes_per_page(self):
#         list_recipes = []
#         # preciso criar varias receitas para fazer o teste
#         # looping para criar
#         for x in range(0, 15):
#             x = self.make_recipe(title=f'recipe0{str(x)}',
#                                  slug=str(x),
#                                  author_data={'username': f'{str(x)}'},
#                                  )
#             list_recipes.append(x.title)

#         # variavel com o total de receitas criado
#         total_recipes_created = len(list_recipes)
#         # variavel com a respota da view
#         response = self.client.get(reverse('recipes:home'))

#         # variavel com o total de receitas exibidas na pagina
#         total_recipes_showed_in_the_page = len(
#             response.context['recipes'].object_list)
#         # vamos primeiro verificar se o numero de receitas criados é maior que o numero de receitas que deve ser exibido # noqa: E501
#         # Assim podemos ter certeza que temos mais que uma pagina de receitas. # noqa: E501
#         # codigp comentado abaixo serve para fazer o test falhar
#         # self.assertGreater(total_recipes_created, 20)
#         self.assertGreater(total_recipes_created, 9)
#         # Abaixo verificamos se o numero de receitas exibidos tem o maximo de 9 por pagina # noqa: E501
#         # para testar o codigo a baixo basta ir na view home e alterar o valor 9 para mais ou para menos em make_pagination # noqa: E501
#         self.assertEqual(total_recipes_showed_in_the_page, 9)

#     def test_pagination_less_than_9_recipes_per_page(self):
#         # vamos testar se quando tivermos um numero de receitas menor que o maximo por pagina (geralmente a ultima pagina) # noqa: E501
#         # o numero correto será exibido
#         # looping para criar 4 receitas
#         list_recipes = []
#         for x in range(0, 4):
#             x = self.make_recipe(title=f'recipe0{str(x)}',
#                                  slug=str(x),
#                                  author_data={'username': f'{str(x)}'}
#                                  )
#             list_recipes.append(x.title)
#         total_list_created = len(list_recipes)
#         # variavel com a resposta da view
#         response = self.client.get(reverse('recipes:home'))
#         # variavel com o total de receitas criado
#         content = response.content.decode('utf-8')
#         # para fazer esse teste falhar abaixo basta alterar na view home o valor de 4 para 9 ou mais # noqa: E501
#         self.assertLess(total_list_created, 9)

#         # codigo comentado abaixo para fazer o teste falhar pois sabemos que "Recipetest" não esta contido no conteudo # noqa: E501
#         # list_recipes.append('Recipetest')

#         # abaixo criei um looping para verifiar se cada receita (valor do titulo) é encontrado no content # noqa: E501
#         for recipe in list_recipes:
#             self.assertIn(recipe, content)
