from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="starting_page"),
    path('books/<slug:slug>',views.book_detail, name="books_details")
]
