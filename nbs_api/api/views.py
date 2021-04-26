from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework import status

def getUser(request):
    return JsonResponse({'user': 'User 1'}, status=status.HTTP_200_OK)

# Create your views here.
