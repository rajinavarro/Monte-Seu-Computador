from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return  HttpResponse(f'hello {nome}')
