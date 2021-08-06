from django.shortcuts import render
from django.http import HttpResponse
from .form import wishlist
def home(request):
    form=wishlist()
    if request.method=='POST':
        form=wishlist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'napsterapp/home.html',context)
def register(request):
    form=wishlist()
    if request.method=='POST':
        form=wishlist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'napsterapp/register.html',context)
def signin(request):
    form=wishlist()
    if request.method=='POST':
        form=wishlist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'napsterapp/signin.html',context)
