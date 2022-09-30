from django.shortcuts import render
from . models import Review

# Create your views here.



def index(request):

    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
       
    }


    return render(request,"todos/index.html",context)

    

def new(request):
    return render(request,"todos/new.html")