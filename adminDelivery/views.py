from django.shortcuts import render
from myapp.views import db
from myapp.models import Product
from delivery.models import Delivery

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
from django.shortcuts import redirect
def login(request):

    return render(request,'admin_delivery_login.html')


def home(request):
    adminemail="Dumstruck"
    adminpass="Dumstruck"
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    if adminemail != email or passw != adminpass  :
        try :
            request.session['admin_delivey_uid']
            delivery_lis=[]
            delivery_id=[]
            delivery_ref=db.collection("delivery")
            delivery_docs=delivery_ref.stream()
            for doc in delivery_docs:
                #print(f'{doc.id} => {doc.to_dict()}')
                delivery=Delivery.from_dict(doc.to_dict())
                delivery_lis.append(delivery)
                delivery_id.append(doc.id)
            comb_lis=zip(delivery_lis,delivery_id)
            return render(request,"admin_delivery_home.html",{"e":email,'comb_lis':comb_lis})

        except:
            message="Invalid credentials"
            return render(request,"admin_delivery_login.html",{"messg":message})
    else :
        request.session['admin_delivey_uid']=adminemail
        delivery_lis=[]
        delivery_id=[]
        delivery_ref=db.collection("delivery")
        delivery_docs=delivery_ref.stream()
        for doc in delivery_docs:
            #print(f'{doc.id} => {doc.to_dict()}')
            delivery=Delivery.from_dict(doc.to_dict())
            delivery_lis.append(delivery)
            delivery_id.append(doc.id)

        comb_lis=zip(delivery_lis,delivery_id)
        return render(request,"admin_delivery_home.html",{"e":email,'comb_lis':comb_lis})

def detail(request,id):
    doc_ref=db.collection("delivery").document(id)
    doc=doc_ref.get()
    if doc.exists:
        delivery=Delivery.from_dict(doc.to_dict())
        print(type(delivery.option))
        print(delivery.option['s'])
        option="s:"+str(delivery.option['s'])+"m:"+str(delivery.option['m'])+"l:"+str(delivery.option['l'])+"xl:"+str(delivery.option['xl'])
    else:
        print(u'No such document!')
    return render(request,"admin_delivery_modify.html",{'delivery':delivery,'option':option,'id':id})

def modify(request):
    documentId=request.POST.get('documentId')
    deliverystate=request.POST.get('deliveryState')
    deliverycode=request.POST.get('deliverycode')
    deliverynum=request.POST.get('deliverynum')
 
    doc_ref=db.collection("delivery").document(documentId)
    doc=doc_ref.get()
    if doc.exists:
        delivery=Delivery.from_dict(doc.to_dict())
  
        option="s:"+str(delivery.option['s'])+"m:"+str(delivery.option['m'])+"l:"+str(delivery.option['l'])+"xl:"+str(delivery.option['xl'])
        # doc_ref.set(
        # Delivery(delivery.brandname,delivery.product_name,checkbox,name,sex,zipcode,adress,adressdetail).to_dict()
        # )
        doc_ref.update({u'deliverystate': deliverystate})
        doc_ref.update({u'deliverycode': deliverycode})
        doc_ref.update({u'deliverynum': deliverynum})
        user_uid=delivery.uid
        user_ref=db.collection("users").document(user_uid).collection("delivery").document(documentId)
        user_ref.update({u'deliverystate': deliverystate})
        user_ref.update({u'deliverycode': deliverycode})
        user_ref.update({u'deliverynum': deliverynum})
        

    else:
        print(u'No such document!')

    doc2=doc_ref.get()
    if doc2.exists:
        delivery2=Delivery.from_dict(doc2.to_dict())
        print(type(delivery2.option))
        print(delivery2.option['s'])
        option2="s:"+str(delivery2.option['s'])+"m:"+str(delivery2.option['m'])+"l:"+str(delivery2.option['l'])+"xl:"+str(delivery2.option['xl'])
        # doc_ref.set(
        # Delivery(delivery.brandname,delivery.product_name,checkbox,name,sex,zipcode,adress,adressdetail).to_dict()
        # )
        
    else:
        print(u'No such document!')


    
    #url="admin/delivery/home/detail/"+documentId+"/"
    return render(request,"admin_delivery_modify.html",{'delivery':delivery2,'option':option2,'id':documentId})
    #return redirect(url)  
    #return render(request,"admin_delivery_home.html")

