from django.urls import path
from .import views

urlpatterns = [
    path('',views.main_view, name='main'),
    path('contacts',views.contacts_view, name='contacts'),
    path('search',views.search_view, name='search'),
    path('create-contact',views.create_contact, name='create-contact'),

    path('update-contact/<str:pk>',views.update_contact, name='update-contact'),
]