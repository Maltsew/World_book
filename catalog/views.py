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

    # count of visits this view, counted with var "session"
    num_visits = requset.session.get('num_visits', 0)
    requset.session['num_visits'] = num_visits + 1

    return TemplateResponse(requset, 'index.html',
                            context={'num_books': num_books,
                                     'num_instances': num_instances,
                                     'num_instances_available': num_instances_available,
                                     'num_author': num_author,
                                     'num_visits': num_visits},
                            )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4
