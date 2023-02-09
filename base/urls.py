from django.urls import path
from .import views

urlpatterns = [
    path('',views.index_view, name='index'),
    path('contacts',views.contacts_view, name='contacts'),
    path('search',views.search_view, name='search'),
]