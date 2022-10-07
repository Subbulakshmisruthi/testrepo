from email.mime import image
from tkinter import Image
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User

def home(request):
    context={}
    return render(request,"home/index.html",context)

def register(request):
    images=image.objects.all()
    context={'images':images}      
    return render(request,'home/register.html',context)
