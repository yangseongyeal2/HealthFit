from django.shortcuts import render
# Create your views here.
from urllib.parse import quote_plus, urlencode
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET
import json
from django.shortcuts import render,get_object_or_404,redirect
import pyrebase
from django.contrib import auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#from firebase_admin import auth

from django.http import HttpResponse


def test(request):
    return render(request,'welcom.html')