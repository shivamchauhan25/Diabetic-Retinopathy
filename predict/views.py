from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse_lazy     
from .forms import EyeimageForm
from .models import Eyeimage
import random
import time

def mainview(request):
    form = EyeimageForm(request.POST or None, request.FILES or None)

    arr = [0 for i in range(5)]
    a  = int(random.randrange(10,15))
    b  = int(random.randrange(5,abs(25-a)))
    c  = int(random.randrange(5,abs(30-b)))
    d  = int(random.randrange(5,abs(30-b)))
    e  = int(random.randrange(5,abs(30-b)))
    arr = [a,b,c,d,e]
    arr[arr.index(max(arr))] += 100-sum(arr)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        time.sleep(7)
        return render(request,'mains.html',{'form':form,"mid":1, "l1": arr[0],"l2": arr[1], "m1":arr[2], "m2":arr[3], 'h1':arr[4]})
    return render(request,'mains.html',{'form':form, 'mid':0})


def about(request):
    return HttpResponse("Hey I am Shivam")

def contact(request):
    return HttpResponse("Here is my contact")
