from populate import base
from book.models import Book, Review

Book.objects.all().delete()
Review.objects.all().delete()