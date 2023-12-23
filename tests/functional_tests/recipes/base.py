import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from utils.browser import make_chrome_browser


class RecipesbaseFunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:  # responsavel por criar o browser
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:  # Responsavel por matar o browser
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=6):
        time.sleep(seconds)
