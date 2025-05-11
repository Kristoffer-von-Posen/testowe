from django.shortcuts import render

# Create your views here.

def index(request):
  import datetime
  now= datetime.datetime.now()
  return render(request, 'Nowyrok/index.html',{
    "newyear": now.month == 1 and now.day == 1
  })