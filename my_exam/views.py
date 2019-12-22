from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
def index(request):
    return HttpResponse("hi, jasuil", 200)

def jsonResponse(request):

    detail1 = {'where1': 'bundan-gu'}
    detail2 = {'where2': 'line'}
    list = [detail1, detail2]
    res = {'jasuil':'1212', 'detail':list}

    return JsonResponse(res)