from django.core.exceptions import ValidationError
from parameterized import parameterized
from test_recipe_base import Recipe, RecipeTestBase


class REcipecategorymodelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='category testing'
        )
        return super().setUp()

    def test_recipe_category_model_string_represetation_is_name_field(self):
        self.assertAlmostEqual(
            str(self.category),
            self.category.name
        )

    def test_recipe_category_model_name_max_length_is_65_chars(self):
        self.category.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
