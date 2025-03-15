from django.shortcuts import redirect
from faker import Faker
from .models import Student
from .serializer import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def view_students(request) -> Response:
    """This function is a view that returns the students data from the 
    database in JSON format."""

    stds_data = Student.objects.all()
    serializer = StudentSerializer(stds_data, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def view_single_student(request, roll) -> Response:
    """This function is a view that returns the `student` data from the 
    database in JSON format."""

    try:
        stds_data = Student.objects.get(roll=roll)
        serializer = StudentSerializer(stds_data)
        return Response(serializer.data, status=200)
    
    except Student.DoesNotExist:
        return Response(status=404)


@api_view(['POST'])
def add_student(request) -> redirect:
    """This function is a view that adds a student to the database."""
    
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return redirect('/api')


def populate_students(request) -> redirect:
    """This function is a view that populates the database with 
    fake students data."""

    fake = Faker()
    for _ in range(10):
        name = fake.name()
        age = fake.random_int(min=18, max=25)
        roll = fake.random_int(min=1, max=100)
        city = fake.city()
        s = Student(name=name, age=age, roll=roll, city=city)
        s.save()

    return redirect('/api')
