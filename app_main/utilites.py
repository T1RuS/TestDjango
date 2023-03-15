from app_main.models import Person
from app_main.serializer import PersonSerializer


def get_flat_data():
    data = Person.objects.all()

    print(PersonSerializer(data).data)
