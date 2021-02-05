from django.shortcuts import render
import requests
from firebase_admin import firestore
from delivery.models import Delivery
from myapp.models import UserModel
import requests


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
    #try:
    print("카트"+request.session['uid'])
    uid=request.session['uid']
    user_ref=db.collection("users").document(uid)
    user_doc=user_ref.get()
    usermodel=None
    checkbox_flag=None
    sex_flag=""
    
       
    if user_doc.exists:
            
        usermodel=UserModel.from_dict(user_doc.to_dict())
        if(usermodel.emailagree=="1"):
            checkbox_flag="동의"
        else:
            checkbox_flag=None
        if(usermodel.sex =="None" or usermodel.sex==""):
            sex_flag=""
        elif (usermodel.sex=="male"):
            sex_flag="male"
        elif (usermodel.sex =="female"):
            sex_flag="female"

    else :
        print("유저모델이없습니다")
    print("섹스플래그"+sex_flag)
    return render(request, 'profile.html',{'uid':uid,'usermodel':usermodel,'checkbox_flag':checkbox_flag,'sex_flag':sex_flag})
    # except:
    #     return render(request, 'signin.html',{'uid':uid})

def modify(request):
    print("수정하기클릭")
    uid=None
   
    #checkbox=request.POST.get('checkbox')
    email=request.POST.get('email')
    emailcheck=request.POST.get('emailcheck')
    password=request.POST.get('password')
    passwordre=request.POST.get('passwordre')
    checkbox=request.POST.get('checkbox')
    name=request.POST.get('name')


    male=request.POST.get('male')
    female=request.POST.get('female')
    gender=request.POST.get('gender')
    sex=None
    if(gender =="male"):
        sex="male"
    if(gender== "female"):
        sex="female"
        
    zipcode=request.POST.get('zipcode')
    adress=request.POST.get('adress')
    adressdetail=request.POST.get('adressdetail')
    adresscf=request.POST.get('adresscf')
    


    print("카트"+request.session['uid'])
    uid=request.session['uid']
    user_ref=db.collection("users").document(uid)

       
    user_ref.set(
        UserModel(email,password,checkbox,name,sex,zipcode,adress,adressdetail).to_dict()
    )
   
    user_doc=user_ref.get()
    usermodel=None
    checkbox_flag=None
    sex_flag=""
    if user_doc.exists:
        usermodel=UserModel.from_dict(user_doc.to_dict())
        if(usermodel.emailagree=="1"):

            checkbox_flag="동의"
        else:
            checkbox_flag=None
    
        
        if(usermodel.sex =="None" or usermodel.sex==""):
            sex_flag=""
        elif (usermodel.sex=="male"):
            sex_flag="male"
        elif (usermodel.sex=="female"):
            sex_flag="female"
          
    else :
        print("유저모델이없습니다")
    print("섹스플래그"+sex_flag)
    return render(request, 'profile.html',{'uid':uid,'usermodel':usermodel,'checkbox_flag':checkbox_flag,'sex_flag':sex_flag})
# except:
#     return render(request, 'signin.html',{'uid':uid})