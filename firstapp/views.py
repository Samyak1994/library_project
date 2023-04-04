from django.shortcuts import render, HttpResponse, redirect
from .models import Book

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'POST':
        print(request.POST)
        bId = request.POST.get('book_id')
        name = request.POST.get('book_name')
        qty = request.POST.get('book_qty')
        price = request.POST.get('book_price')
        author = request.POST.get('book_author')
        is_published = request.POST.get('book_is_published')
        print(name,qty,price,author,is_published)
        if is_published == 'Yes':
            is_published = True
        elif is_published == 'No':
            is_published = False

        if not bId:
            #agar create krna hotoh ye use krna h
            Book.objects.create(name= name,qty=qty , price=price , author= author , is_published=is_published)
        else:
            #agar update krna hototoh ye use krna h
            book_obj= Book.objects.get(id=bId)
            book_obj.name = name
            book_obj.qty = qty
            book_obj.price = price
            book_obj.author = author
            book_obj.is_published = is_published

            book_obj.save()

        return redirect('home_page')

        # return HttpResponse('SUBMITTED')
    elif request.method == 'GET':
        print(request.GET)
        # return render(request , 'home.html'  ,context={'all_book' : Book.objects.all()})
        return render(request , 'home.html' )



@csrf_exempt
def show_book(request):
    return render(request, 'show_books.html', context={'books': Book.objects.filter(is_active = True)})



@csrf_exempt
def update_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    return render(request , "home.html" ,context={'single_book' : book_obj})

@csrf_exempt
def delete_book(request,pk):
    Book.objects.get(id=pk).delete()
    return redirect('all_active_book') 

@csrf_exempt
def soft_delete_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = False
    book_obj.save()
    return redirect('inactive_book') 



@csrf_exempt
def show_inactive_book(request):
    return render(request, 'show_books.html', context={'books': Book.objects.filter(is_active = False),'inactive': True})

@csrf_exempt
def restore_book(request,pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.is_active = True
    book_obj.save()
    return redirect('all_active_book') 
