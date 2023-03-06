from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def server_testing(request):
    data = {"status": "Servidor funcionando!!"}
    return JsonResponse(data)