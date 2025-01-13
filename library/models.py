from django.db import models

class Library(models.Model):
    book_name = models.CharField(max_length=255)
    book_id = models.CharField(max_length=100, unique=True)
    author_name = models.CharField(max_length=255)
    STATUS_CHOICES = [('Available', 'Available'), ('Issued', 'Issued')]
    book_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Available')
    card_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.book_name
