from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    tn=input('enter topic')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    return HttpResponse('topic created')
def insert_Webpage(request):
    tn=input('enter webpages')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    n=input('enter name')
    u=input('enter url')
    Wo=Webpage.objects.get_or_create(topic_name=To,name=n,url=u)[0]
    Wo.save()
    return HttpResponse('Webpage is created')
def insert_AccessRecord(request):
    n=input('enter name')
    Wo=Webpage.objects.get_or_create(name=n)[0]
    Wo.save()
    a=input('enter author')
    d=input('enter value')
    Ao=AccessRecord.objects.get_or_create(name=Wo,author=a,date=d)[0]
    Ao.save()
    return HttpResponse('Accessrecords')
