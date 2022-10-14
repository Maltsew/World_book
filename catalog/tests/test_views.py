import datetime
import unittest

from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import Author
from django.contrib.auth.models import User
from http import HTTPStatus


class TestIndexView(TestCase):
    def test_uses_index_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_displays_items_for_main_page(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Main Page')

    def test_session_counting_of_visits(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'You visit this page')


class TestBookView(TestCase):
    def test_uses_book_template(self):
        response = self.client.get(reverse('books'))
        self.assertTemplateUsed(response, 'catalog/book_list.html')


class TestAuthorView(TestCase):
    def test_uses_author_template(self):
        response = self.client.get(reverse('authors'))
        self.assertTemplateUsed(response, 'catalog/author_list.html')


class TestAddAuthorView(TestCase):
    def test_uses_add_author_template(self):
        response = self.client.get(reverse('authors_add'))
        self.assertTemplateUsed(response, 'catalog/authors_add.html')

    @unittest.skip
    def test_add_author_saves_valid_object(self):
        valid_data = {"first_name": "Aaa", "last_name": "Bbb", "date_of_birth": datetime.date.today(),
                      "date_of_death": datetime.date.today()}
        user = User.objects.create()
        self.client.force_login(user)
        response = self.client.post('/create', data=valid_data)
        self.assertEqual(response, HTTPStatus.FOUND)
