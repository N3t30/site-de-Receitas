from django.core.exceptions import ValidationError
from parameterized import parameterized
from test_recipe_base import Recipe, RecipeTestBase


class Recipemodelstest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    # extraindo no metodo

    def make_recipe_no_defaults(self, slug_content='recipe-slug-02'):
        recipe = Recipe(
            category=self.make_category(name='test default category'),
            author=self.make_author(username='newuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug=slug_content,
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_lenght(self, field, max_lenght):
        setattr(self.recipe, field, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not false',)

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is published is not false',
        )

    def test_recipe_string_representation(self):
        self.recipe.title = 'testing Representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertAlmostEqual(str(self.recipe), 'testing Representation')

    def test_recipe_slug_name_is_not_repeated(self):
        with self.assertRaises(ValidationError):
            self.make_recipe_no_defaults('recipe-slug')
