from django.shortcuts import render
import requests
from firebase_admin import firestore
from delivery.models import Delivery


db=firestore.client()
# Create your views here.
def mypage(request):
    uid=None
    try:
        print("카트"+request.session['uid'])
        uid=request.session['uid']
        return render(request, 'mypage.html',{'uid':uid})
    except:
        return render(request, 'signin.html',{'uid':uid})
   

def orderinfo(request):

    uid=None
    try:
        print("카트"+request.session['uid'])
        uid=request.session['uid']
        user_doc=db.collection("users").document(uid).collection("delivery")
        user_alldocs=user_doc.stream()
        print("??")
        deliverylist=[]
        for doc in user_alldocs:
            delivery=Delivery.from_dict(doc.to_dict())
            #print(delivery)
            deliverylist.append(delivery)
        
        return render(request, 'orderinfo.html',{'uid':uid,'deliverylist':deliverylist})
    except:
        return render(request, 'signin.html',{'uid':uid})

def profile(request):
    uid=None
    try:
        print("카트"+request.session['uid'])
        uid=request.session['uid']
        return render(request, 'profile.html',{'uid':uid})
    except:
        return render(request, 'signin.html',{'uid':uid})