from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
   # text = "<h1>welcome to my app number %s!</h1>"
   # return HttpResponse(text)
   today = datetime.datetime.now().date()
   return render(request, "hello.html", {"today": today})
   