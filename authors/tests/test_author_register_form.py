#  teste unitario é um teste onde voce testa uma coisa exclusivamente
#  teste de integração onde faz tudo se intregar no caso view, tamplate, urls e etc # noqa: E501
from django.test import TestCase
from parameterized import parameterized

from authors.forms import RegisterForm


class AuthorRegisterFormUniTest(TestCase):
    @parameterized.expand([
        ('username', 'your username'),
        ('email', 'Ex.: jhonExample@gmail.com'),
        ('first_name', 'Ex.: Jhon'),
        ('last_name', 'Ex.: wick'),
        ('password', 'type your password'),
        ('password2', 'repeat your password'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('username', (
            'Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.')),  # noqa: 501
        ('email', 'The email must be valid'),
        ('password', (
            'Password must havee at least one upprtcase letter,'
            'one loweercase letter aaand one number. the length should be '
            'at least 8 characters.'
        )),
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

    @parameterized.expand([
        ('username', 'Username'),
        ('first_name', 'First name'),
        ('last_name', 'Last name'),
        ('email', 'E-mail'),
        ('password', 'Password'),
        ('password2', 'Password2'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)
