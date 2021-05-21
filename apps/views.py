# Create your views here.
from django.shortcuts import render


# 首页
def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def register(request):
    return render(request, 'register/register.html')


def getassets(request):
    return render(request, 'getassets/getassets.html')
