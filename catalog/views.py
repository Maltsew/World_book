from django.shortcuts import render
from django.http import HttpResponse

def index(requset):
    return HttpResponse("Main page Books World!")
