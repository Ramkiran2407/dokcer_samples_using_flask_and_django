from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.

def basic(request):
    return HttpResponse ("welcome to Django Docker")

def database_func(request):
    return JsonResponse({"hello":"reponse"})