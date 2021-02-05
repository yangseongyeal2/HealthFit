from django.shortcuts import render
from firebase_admin import firestore
from delivery.models import Delivery
from myapp.models  import Cart,Product

db=firestore.client()


# Create your views here.
def index(request):

    return render(request,'index.html')
   
def getdata(request,option,price,username,phonenum,address,uid,delivery_message,product_id):
  

    prd_ref = db.collection(u'product').document(product_id)

    prd_docs = prd_ref.get()
    if prd_docs.exists:
        products=Product.from_dict(prd_docs.to_dict())
        img=products.downloadurl
        brandname=products.brand
        product_name=products.name
       

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
            ,img
            ,product_id
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
            ,img
            ,product_id
            ).to_dict()   
        )

    else:
        print(u'No such document!')



    

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
        ,cart.downloadurl
        ,cart.documentId
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
        ,cart.downloadurl
        ,cart.documentId
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

