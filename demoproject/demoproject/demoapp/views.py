from django.http import HttpResponse
from django.shortcuts import render
from.models import Teams

# Create your views here.
def demo(request):
    obj=Teams.objects.all()
    return render(request,"index.html",{'result':obj})



