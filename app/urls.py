from django.urls import path
from . import views
urlpatterns = [
    path('view', views.view_students, name='view_std'),
    path('view/<int:roll>', views.view_single_student, name='view_single_Std'),
    path('add', views.add_student, name='add_std'),
    path('update/<int:roll>', views.update_student, name='update_std'),
    path('delete/<int:roll>', views.delet_student, name='update_std'),
    path('populate', views.populate_students, name='populate_std'),
]
