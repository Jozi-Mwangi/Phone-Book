from django.urls import path
from .import views

urlpatterns = [
    path('',views.main_view, name='main'),
    path('search',views.search_view, name='search'),
    path('create-contact',views.create_contact, name='create-contact'),

    path('contact/<str:pk>',views.contact_view, name='contact'),
    path('update-contact/<str:pk>',views.update_contact, name='update-contact'),
]