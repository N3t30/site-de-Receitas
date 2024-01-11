from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import AuthorBaseTest


class AuthorRegisterTest(AuthorBaseTest):
    def get_by_placeholder(self, web_element, placeholder):
        return web_element.find_element(
            By.XPATH, f'//input[@placeholder="{placeholder}"]')

    def fiil_form_dummy_data(self, form):

        # Do formulario estou selecionando todos os inputs
        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(" " * 20)

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )

    def form_fields_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.fiil_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('test@gmail')

        callback(form)
        return form

    def test_empty_first_name_message(self):
        def callback(form):
            first_name_field = self.get_by_placeholder(form, 'Ex.: John')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your first name', form.text)
        self.form_fields_test_with_callback(callback)

    def test_empty_last_name_error_message(self):
        def callback(form):
            last_name_field = self.get_by_placeholder(form, 'Ex.: Doe')
            last_name_field.send_keys(' ')
            last_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your last name', form.text)
        self.form_fields_test_with_callback(callback)

    def test_empty_username_error_message(self):
        def callback(form):
            username_field = self.get_by_placeholder(form, 'Your username')
            username_field.send_keys(' ')
            username_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('This field must not be empty', form.text)
        self.form_fields_test_with_callback(callback)

    def test_invalid_email_error_message(self):
        def callback(form):
            email_field = self.get_by_placeholder(form, 'Your e-mail')
            email_field.send_keys(' ')
            email_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('The e-mail must be valid.', form.text)
        self.form_fields_test_with_callback(callback)

    def test_passwords_do_not_match(self):
        def callback(form):
            password = self.get_by_placeholder(form, 'Type your password')
            password2 = self.get_by_placeholder(form, 'Repeat your password')
            password.send_keys('Slipkn@t123')
            password2.send_keys('Slipkn@t123_01')
            password2.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('password and password2 must be equal', form.text)
        self.form_fields_test_with_callback(callback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        self.get_by_placeholder(form, 'Ex.: John').send_keys('First name')
        self.get_by_placeholder(form, 'Ex.: Doe').send_keys('Last Name')
        self.get_by_placeholder(form, 'Your username').send_keys('My_sername')
        self.get_by_placeholder(
            form, 'Your e-mail').send_keys('Example@gmail.com')
        self.get_by_placeholder(
            form, 'Type your password').send_keys('Slipkn@t123')
        self.get_by_placeholder(
            form, 'Repeat your password').send_keys('Slipkn@t123')

        form.submit()

        self.assertIn(
            'your user is created, please login.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

        self.sleep(10)
