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
    #  Testando se a aplicação levanta um erro 404 caso o usuario faça um get

    def test_login_create_eraises_404_if_not_post_method(self):
        # fazendo um get para o login create
        self.browser.get(
            self.live_server_url +
            reverse('authors:login_create'))

        self.assertIn(
            'Not Found ',
            self.browser.find_element(By.TAG_NAME, 'body').text

        )

        # self.sleep()

    def test_form_not_valid(self):
        string_password = ' '
        user = User.objects.create_user(
            username=' ', password=string_password)
        # Usuario abre a pagina
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # Usuario vê o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # Tenta enviar valores vazios ou inexistente
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # Envia o formulario
        form.submit()

        # vê uma menssagem de erro na tela
        self.assertIn(
            'Error to validate form data',
            self.browser.find_element(By.TAG_NAME, 'body').text

        )

        self.sleep()
