from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("우분투 장고 테스트 중입니다")

    
        
