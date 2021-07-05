from django.urls import path

from . import views

app_name = 'triangle'
urlpatterns = [
    path('', views.triangle, name='triangle'),
    # Home task 7. ModelForm for Person
    path('person/', views.create_person, name='person'),
    path('person/<int:pk>/', views.update_person, name='update-person'),
]
