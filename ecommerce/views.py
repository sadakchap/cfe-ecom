from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return render(req,'index.html',{})
def about(req):
    return render(req,'about.html',{})
def contact(req):
    return render(req,'contact.html',{})
