from django.contrib.auth.models import User
from rest_framework import serializers
from app_main.models import Person, Book


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username']


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Book
        fields = ['id', 'name']


class PersonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    user = UserSerializer()
    book = serializers.SerializerMethodField()
    book_comment = serializers.CharField(source='book.comment')

    def get_book(self, obj):
        return f'{obj.book.name} - {obj.book.comment}'

    class Meta:
        model = Person
        fields = ['id', 'user', 'book', 'book_comment']
