from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    books_arr = Book.objects.all()
    num_books = books_arr.count()
    avg_rating = books_arr.aaggregate(Avg("rating"))
    return render(request, 'book_outlet/index.html',{
        "books":books_arr, 
        "total_number_of_books":num_books,
        "average_rating":avg_rating
    })


def book_detail(request,slug):
    book = get_object_or_404(Book,slug=slug)
    return render(request,'book_outlet/book_detail.html',{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestselling":book.is_bestselling
    })