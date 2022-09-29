from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
# admin.site.register(BookInstance)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre', 'display_language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Books Instance', {
            'fields': ('book', 'imprint', 'stock_num')
        }),
        ('Status and date of ends', {
            'fields': ('status', 'due_back')
        })
    )
