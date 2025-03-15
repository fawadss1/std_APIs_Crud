from django.urls import path
from .views import populate_students, view_students, add_student, view_single_student

urlpatterns = [
    path('view', view_students, name='view_std'),
    path('view/<int:roll>', view_single_student, name='view_single_Std'),
    path('add', add_student, name='add_std'),
    path('populate', populate_students, name='populate_std'),
]