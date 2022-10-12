import datetime
from django.test import TestCase
from django.urls import resolve
from catalog.views import index
from catalog.models import Genre, Language, Author, Book, Status
from datetime import date
from django.urls import reverse


class GenreModelTest(TestCase):
    """Check genre"""

    def test_saving_and_retrieving_genres(self):
        first_genre = Genre()
        first_genre.name = 'Detective'
        first_genre.save()

        saved_genres = Genre.objects.all()
        self.assertEqual(saved_genres.count(), 1)

        first_saved_genre = saved_genres[0]
        self.assertEqual(first_saved_genre.name, 'Detective')


class LanguageModelTest(TestCase):
    """Test language model"""

    def test_saving_and_retrieving_languages(self):
        first_language = Language()
        first_language.lang = 'English'
        first_language.save()

        second_language = Language()
        second_language.lang = 'Russian'
        second_language.save()

        saved_languages = Language.objects.all()
        self.assertEqual(saved_languages.count(), 2)

        first_saved_language = saved_languages[0]
        second_saved_language = saved_languages[1]
        self.assertEqual(first_saved_language.lang, 'English')
        self.assertEqual(second_saved_language.lang, 'Russian')


class AuthorModelTest(TestCase):
    """Test author model"""

    def test_saving_and_retrieving_author(self):
        author = Author()
        author.first_name = 'Vladimir'
        author.last_name = 'Lenin'
        author.date_of_birth = '1870-4-22'
        author.date_of_death = '1924-1-21'
        author.save()
        saved_author = Author.objects.all()
        # saved_author is a queryset, take its first record
        first_saved_author = saved_author[0]
        self.assertEqual(saved_author.count(), 1)
        self.assertEqual(first_saved_author.first_name, 'Vladimir')
        self.assertEqual(first_saved_author.last_name, 'Lenin')
        self.assertEqual(first_saved_author.date_of_birth, datetime.date(1870, 4, 22))
        self.assertEqual(first_saved_author.date_of_death, datetime.date(1924, 1, 21))


class BookModelTest(TestCase):
    """Test book model"""

    def test_saving_and_retrieving_book(self):
        book = Book.objects.create(title='Don Quixote',
                                   summary='Alonso Quixano, a retired country gentleman in his fifties, lives',
                                   isbn='9780744525021')
        book.save()
        temp1 = book.genre.create(name='Novel')
        temp1.save()
        temp2 = book.language.create(lang='English')
        temp2.save()
        temp3 = book.author.create(first_name='Migel de Cervantes', last_name='Aaa',
                                  date_of_birth=datetime.date(1870, 4, 22),
                                  date_of_death=datetime.date(1924, 1, 21))
        temp3.save()
        saved_book = Book.objects.all()
        self.assertEqual(saved_book.count(), 1)
        self.assertEqual(book.title, 'Don Quixote')
        self.assertEqual(book.summary, 'Alonso Quixano, a retired country gentleman in his fifties, lives')
        self.assertEqual(temp1.name, 'Novel')
        self.assertEqual(temp2.lang, 'English')
        self.assertEqual(temp3.first_name, 'Migel de Cervantes')
        self.assertEqual(temp3.last_name, 'Aaa')
        self.assertEqual(temp3.date_of_birth, datetime.date(1870, 4, 22))
        self.assertEqual(temp3.date_of_death, datetime.date(1924, 1, 21))

    """it is better to hold testing of display functions with the help of Django test client.
    One of ways is assertContains responses with get method from admin panel and check tags"""

    def create_book(self):
        book = Book.objects.create(title='Don Quixote',
                                   summary='Alonso Quixano, a retired country gentleman in his fifties, lives',
                                   isbn='9780744525021')
        book.save()
        return book

    def test_get_absolut_url(self):
        w = self.create_book()
        response = self.client.get(reverse('book-detail', args=[w.pk, ]))
        self.assertEqual(response.status_code, 200)


class StatusModelTest(TestCase):
    """"""

    def test_saving_and_retrieving_status(self):
        status = Status.objects.create(status_name='In stock')
        status.save()
        saved_status = Status.objects.all()
        self.assertEqual(saved_status.count(), 1)
        self.assertEqual(status.status_name, 'In stock')


class BookInstanceModelTest(TestCase):
    """"""

    # book = BookModelTest.create_book()

