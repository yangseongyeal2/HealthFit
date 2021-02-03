from django.shortcuts import render
from firebase_admin import firestore
from delivery.models import Delivery
from myapp.models  import Cart

db=firestore.client()


# Create your views here.
def index(request):

    return render(request,'index.html')
   
def getdata(request,brandname,product_name,option,price,username,phonenum,address,uid,delivery_message):
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
        ,delivery_message 
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
        ,delivery_message 
        ).to_dict()   
    )

    return render(request,'getdata.html')

def cart_order_complete(request,total_price,username,phonenumber,address,uid,delivery_message):
    cart_ref=db.collection("users").document(uid).collection('cart')
    cart_alldoc=cart_ref.stream()
    for doc in cart_alldoc:
        cart=Cart.from_dict(doc.to_dict())
        doc_ref=db.collection("delivery")
        doc_ref_random=db.collection("delivery").document()
        doc_ref_random.set(
        Delivery(
        cart.brand
        ,cart.name
        ,cart.sizedic
        ,cart.price
        ,username
        ,phonenumber
        ,address
        ,firestore.SERVER_TIMESTAMP
        ,"배송전"
        ,""
        ,""
        ,uid
        ,delivery_message 
        ).to_dict()   
        )

        user_doc=db.collection("users").document(uid).collection("delivery").document(doc_ref_random.id)
        user_doc.set(
        Delivery(
        cart.brand
        ,cart.name
        ,cart.sizedic
        ,cart.price
        ,username
        ,phonenumber
        ,address
        ,firestore.SERVER_TIMESTAMP
        ,"배송전"
        ,""
        ,""
        ,uid
        ,delivery_message 
        ).to_dict()   
        )
    #for문끝
   
    
   
    def delete_collection(coll_ref, batch_size):
        deldocs = coll_ref.limit(batch_size).stream()
        deleted = 0

        for doc in deldocs:
            print(f'Deleting doc {doc.id} => {doc.to_dict()}')
            doc.reference.delete()
            deleted = deleted + 1

        if deleted >= batch_size:
            return delete_collection(coll_ref, batch_size)
    
    delete_collection(cart_ref,3)



    return render(request,'getdata.html')

