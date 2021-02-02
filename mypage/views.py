from django.shortcuts import render
import requests

# Create your views here.
def mypage(request):
    uid=None
    try:
        print("카트"+request.session['uid'])
        uid=request.session['uid']
        return render(request, 'mypage.html',{'uid':uid})
    except:
        return render(request, 'signin.html',{'uid':uid})
   