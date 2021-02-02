from django.shortcuts import render
from firebase_admin import firestore
from delivery.models import Delivery

db=firestore.client()


# Create your views here.
def index(request):

    return render(request,'index.html')
   
def getdata(request,brandname,product_name,option,price,username,phonenum,address,uid):
    print("브랜드이름:"+brandname)
    print("product_name:"+product_name)
    print("option:"+option)
    #print("price:"+price)
    print("username:"+username)
    #print("phonenum:"+phonenum)
    print("address:"+address)
    doc_ref=db.collection("delivery")
    doc_ref_random=db.collection("delivery").document()
    doc_ref_random.set(
        Delivery(
        brandname
        ,product_name
        ,option
        ,price
        ,username
        ,phonenum
        ,address
        ,firestore.SERVER_TIMESTAMP
        ,"배송전"
        ,""
        ,""
        ,uid 
        ).to_dict()   
    )
    user_doc=db.collection("users").document(uid).collection("delivery").document(doc_ref_random.id)
    user_doc.set(
          Delivery(
        brandname
        ,product_name
        ,option
        ,price
        ,username
        ,phonenum
        ,address
        ,firestore.SERVER_TIMESTAMP
        ,"배송전"
        ,""
        ,""
        ,uid 
        ).to_dict()   
    )

    return render(request,'getdata.html')
