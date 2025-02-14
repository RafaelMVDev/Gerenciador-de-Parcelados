from django.shortcuts import render

# Create your views here.


def login(response):
    return render(response,'login\login.html')


def request(response):
    if response.method == "POST":
        print("CHEGOU EM FORMATO DE POST...")
        return '<html><head> </head> <body> </body></html>'
    else:
        return '<html><head> </head> <body> </body></html>'