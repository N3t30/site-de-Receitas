from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthorLogoutTest(TestCase):
    # usuário de teste tenta sair usando o método get
    def test_user_tries_to_logout_using_get_method(self):
        # Criando um usuario
        User.objects.create_user(username='My_user', password='pass')
        # O Client do django já tem um login
        self.client.login(username='My_user', password='pass')

        # estou usando o get pq estou testando com o usuario tentando fazer login com get # noqa 501
        reponse = self.client.get(
            reverse('authors:logout'),
            follow=True
        )

        self.assertIn(
            'invalid logout request',
            reponse.content.decode('utf-8')
        )

    def test_user_tries_to_logout_another_user(self):
        # Criando um usuario
        User.objects.create_user(username='My_user', password='pass')
        # O Client do django já tem um login
        self.client.login(username='My_user', password='pass')

        # Esse tem que ser com POST para não cair no erro
        reponse = self.client.post(
            reverse('authors:logout'),
            # No data vou passar outro usuario
            data={
                # Enviar outro username sem estar logado
                'username': 'another_user'
            },
            follow=True
        )

        self.assertIn(
            'invalid logout user',
            reponse.content.decode('utf-8')
        )

    def test_user_can_logout_successfully(self):
        # Criando um usuario
        User.objects.create_user(username='My_user', password='pass')
        # O Client do django já tem um login
        self.client.login(username='My_user', password='pass')

        # Esse tem que ser com POST para não cair no erro
        reponse = self.client.post(
            reverse('authors:logout'),
            data={
                # Aqui o usuario tem que ser o mesmo
                'username': 'My_user'
            },
            follow=True
        )

        self.assertIn(
            'logged out successfully',
            reponse.content.decode('utf-8')
        )
