from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    """Model for storage books genre"""
    name = models.CharField(max_length=200, help_text="Please enter genre", verbose_name="Genre")

    def __str__(self):
        return self.name


class Language(models.Model):
    """Model for storage books language"""
    lang = models.CharField(max_length=20, help_text="Enter book language", verbose_name="Language")

    def __str__(self):
        return self.lang


class Author(models.Model):
    """Model for storage info about author"""
    first_name = models.CharField(max_length=100, help_text="Enter authors name", verbose_name="Authors name")
    last_name = models.CharField(max_length=100, help_text="Enter authors last name", verbose_name="Authors last name")
    date_of_birth = models.DateField(help_text="Enter authors date of birth",
                                     verbose_name="Date of birth", null=True, blank=True)
    date_of_death = models.DateField(help_text="Enter authors date of death",
                                     verbose_name="Date of death", null=True, blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    """Model for storage info about books. Fields """
    title = models.CharField(max_length=200, help_text="Enter books title", verbose_name="Book title")
    genre = models.ManyToManyField("Genre", help_text="Book genre", verbose_name="Book genre")
    language = models.ManyToManyField("Language", help_text="Book language", verbose_name="Book language")
    author = models.ManyToManyField("Author", help_text="Book author", verbose_name="Book author")
    summary = models.TextField(max_length=1000,
                               help_text="Enter a short description about this book", verbose_name="A summary")
    isbn = models.CharField(max_length=13,
                            help_text="Enter a thirteen-place symbol index", verbose_name="ISBN of book")

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Author'

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    display_genre.short_description = 'Genre'

    def display_language(self):
        return ', '.join([language.lang for language in self.language.all()])

    display_language.short_description = 'Language'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """returns a URL for access a determine book"""
        # return reverse('catalog:books', args=[str(self.id)])
        return f"/books/{str(self.id)}/"


class Status(models.Model):
    """Model for storage info about actual status instance of books in store"""
    status_name = models.CharField(max_length=20,
                                   help_text="Enter the status of a copy of the book",
                                   verbose_name="Status of a copy of the book")

    def __str__(self):
        return self.status_name


class BookInstance(models.Model):
    """Model for storage existing status of books"""
    # TO-DO Check Meta class for sorting
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    stock_num = models.CharField(max_length=20, help_text="Enter stock number of a copy of the book")
    imprint = models.CharField(max_length=200, help_text="Enter the publishing house and year of a book",
                               verbose_name="Publishing house")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, help_text="Enter a status of a copy of the book",
                               verbose_name="Status of a copy of the book")
    due_back = models.DateField(null=True, blank=True, help_text="Enter date the status change",
                                verbose_name="Date of change the status")

    def __str__(self):
        return f"{self.book} {self.stock_num} {self.status}"
