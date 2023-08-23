from django.shortcuts import render,HttpResponse

from . import models

# Create your views here.
def index(request):
    context = {}
    
    news = models.News.objects.all()
    
    for newss in news:
        newss.Author.rank = getModelChoice(newss.Author.rank, models.Rank)
    
    context["news"] = news
    
    
    return render (request,"blank.html", context)

def Home(request):
    return render (request,"index.html", )

def About(request):
    return render (request,"about.html")

def Contact(request):
    return render (request,"contact.html")

def getModelChoice(num, choices):
    for choice in choices:
        if choice[0] == num:
                return choice[1]
