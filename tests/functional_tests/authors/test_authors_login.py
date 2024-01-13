import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By

from .base import AuthorBaseTest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorBaseTest):
    # dados válidos do usuário de teste podem fazer login com sucesso
    def test_user_valid_can_login_successfully(self):
        # criando um usuario
        # dados obrigatorios password e username
        string_password = 'pass'
        user = User.objects.create_user(
            username='my_user', password=string_password)
        # Usuário abre a pagina de login
        # O ( Reverse ) faz eu ter uma url dinamica caso ela mude
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # Usuario vê o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # Usuario digita seu usuario e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # Usuario enviar o formulario
        form.submit()

        # Usuario vê a mensagem de login e seu nome
        self.assertIn(
            f'your are logged in with {user.username}',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
