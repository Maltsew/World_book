from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(requset):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()

    num_author = Author.objects.all().count()

    return TemplateResponse(requset, 'index.html',
                            context={'num_books': num_books,
                                     'num_instances': num_instances,
                                     'num_instances_available': num_instances_available,
                                     'num_author': num_author},
                            )


class BookListView(generic.ListView):
    model = Book
