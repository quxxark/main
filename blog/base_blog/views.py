from django.shortcuts import render
from django.http import HttpResponse


def postsList(request):
    return HttpResponse('<h1>Initial page</h1>')
