import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.
def index(request):
    return HttpResponse("Hello")

def addBook(request):
    book1 = Book(name="Yellow Sun", pageNumber="20", publishDate= "2015-11-23")
    book1.save()
    return HttpResponse("new book")

def allBooks(request):
    bookKist = Book.objects.all()
    for x in bookKist:
        if (x.publishDate>datetime.date(2018, 1, 1)):
            print(x)
    return HttpResponse('All Books')

