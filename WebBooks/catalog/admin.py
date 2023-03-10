from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance
#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('list_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

