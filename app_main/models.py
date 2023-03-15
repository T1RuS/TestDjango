from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='name')
    comment = models.CharField(max_length=100, null=True, blank=True, verbose_name='comment')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Person(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='User')
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Book')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'Person'
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
