import json

from django.shortcuts import render
from rest_framework.response import Response

from app_main.models import Person
from app_main.serializer import PersonSerializer


def get_flat_data(request):
    data = Person.objects.all()

    print(json.loads(json.dumps(PersonSerializer(data, many=True).data)))
    return Response(status=200)

