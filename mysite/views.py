# from django.http import HttpResponse

# def index(request):
#     return HttpResponse('''<h1>Hello</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django Code with harry</a>''')


# def about(request):
#     return HttpResponse("about Hello")

from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def removepunc(request):
    gjtext(request.GET.get('text','default'))
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove")

def spaceremove(request):
    return HttpResponse("spaceremove <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount")

