from catalog.forms import AuthorsForm
from django.test import TestCase
import datetime


class TestAuthorsForm(TestCase):
    def test_form_is_valid(self):
        form_data = {"first_name": "Aaa", "last_name": "Bbb", "date_of_birth": datetime.date.today(),
                     "date_of_death": datetime.date.today()}
        form = AuthorsForm(data=form_data)
        self.assertTrue(form.is_valid())
