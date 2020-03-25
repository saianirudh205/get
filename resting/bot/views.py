from django.shortcuts import render
#from .bots import BotConfig
from django.http import HttpResponse
from bot.anirudh.loaded import chat2
from bot.anirudh.messgae import get,clear
import os
import json as js
# Create your views here.
# Create your views here.
def home(request):
    clear()
    return render(request,'home.html',{'display':'Waiting for Your text'})
def chat(request):
    a=request.POST['msg']
    c=chat2(a)
    ani={}
    h=get(ani,a,c)
    return render(request,'next.html',{'man':h['doc']})
