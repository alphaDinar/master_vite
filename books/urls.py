from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('api/get_books', views.GetBooksAPI.as_view()),
]
