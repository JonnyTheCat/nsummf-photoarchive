from django.shortcuts import render



def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contacts.html')



def login(request):
    return render(request, 'base/login.html')

def register(request):
    return render(request, 'base/register.html')