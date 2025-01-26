from django.shortcuts import render
from django.http import HttpResponse
#from Pages import *
# Create your views here.


def start_page(response):
    return render(response,'gerenciador\start_page.html')

def next_page(response):
    return render(response,'gerenciador\test_page.html')