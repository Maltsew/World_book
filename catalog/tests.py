from django.test import TestCase
from django.urls import resolve
from catalog.views import index
from catalog.models import Genre


class MainPageTest(TestCase):
    """"""

    def test_root_url_resolves_main_page(self):
        """Test unites: checking root url "/" to compliance index view and
         index view compliance index.html template"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
