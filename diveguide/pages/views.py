from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the pages index.")
