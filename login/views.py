from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(response):
    return render(response,'login\login.html')
    

def request(response):
    if response.method == "POST":
        print("CHEGOU EM FORMATO DE POST...", response.POST)
        return HttpResponse()
    else:
        return HttpResponse()
