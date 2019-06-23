from django.contrib import admin
from book.models import Book , Review

class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'publisher', 'publicationDate', 'price', 'pubDateTime']
 
    class Meta:
        model = Book


class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['pubDateTime', 'book', 'review', 'score']
    list_display_links = ['book']
    list_filter = ['book', 'review', 'score']
    search_fields = ['review']
    list_editable = ['review']
 
    class Meta:
        model = Review


admin.site.register(Book, BookModelAdmin)
admin.site.register(Review, ReviewModelAdmin)