from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField(max_length=10000)
    author = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    publicationDate = models.CharField(max_length=128)
    price = models.IntegerField()
    pubDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['-pubDateTime']

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.CharField(max_length=30)
    score = models.IntegerField(range(1,5))
    pubDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title + '-' + str(self.id)
    
    class Meta:
        ordering = ['pubDateTime']