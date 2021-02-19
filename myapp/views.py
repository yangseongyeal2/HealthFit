
from django.shortcuts import render,get_object_or_404,redirect
import pyrebase
#from pyrebase import pyrebase
#from django.contrib import auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
#from firebase_admin import auth
from .models import Product
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserModel
from .models import Cart
from delivery.models import Delivery
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

# from google_images_download import google_images_download   #importing the library

# response = google_images_download.googleimagesdownload()   #class instantiation

# arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
# paths = response.download(arguments)   #passing the arguments to the function
# print(paths)   #printing absolute paths of the downloaded images



config={
    'apiKey': "AIzaSyAFN2apSBQwHIiGioEKyyQORxceIR22VMs",
    'authDomain': "healthstore-de3c3.firebaseapp.com",
    'databaseURL': "https://healthstore-de3c3-default-rtdb.firebaseio.com",
    'projectId': "healthstore-de3c3",
    'storageBucket': "healthstore-de3c3.appspot.com",
    'messagingSenderId': "838060678239",
    'appId': "1:838060678239:web:d861eca1e8639cc3a14fea",
    'measurementId': "G-3T3MCBWTZ8"
}
firebase =pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()


####
cred=credentials.Certificate('myapp/service-account.json')
firebase_admin.initialize_app(cred)
db=firestore.client()
#recentview_lis=[]



# Create your views here.
def home(request):
    uid=None
    name=""
    print("홈시작")
    documentId=request.session.get('RecentView',False)
    try:
        request.session['RecentView']
        recentview_lis=request.session['RecentView']
    except :
        request.session['RecentView']=[]
    


    try:
        print("홈에서"+request.session['uid'])
        uid=request.session['uid']
        user_ref=db.collection("users").document(uid)
        user_doc=user_ref.get()
        if user_doc.exists:
            print(u'Document data: {}'.format(user_doc.to_dict()))
            usermodel=UserModel.from_dict(user_doc.to_dict())
            name=usermodel.name
        else:
            print(u'No such document!')

    except:
        print("로그인안댐")
        
    
    
  
   
   
    return render(request,'home.html',{'uid':uid,'name':name,'documentId':documentId})

    

def hello(request):
    doc_ref=db.collection("product")
    # doc_ref_random=db.collection("product").document()
    # doc_ref_random.set(
    #     Product('양성열','25',doc_ref_random).to_dict()
    # )
    # # doc_ref.document().set(
    # #     Product('남종경','25').to_dict()
    # # )
    
    # try:
    #     docs=doc_ref.document('test').get()
    #     print('Document data: {}'.format(docs.to_dict()))
    #     #print(product)
    #     products=Product.from_dict(docs.to_dict())
       
    # except:
    #     print('No such document!')

   #파이어스토어 데이터 불러오기
    alldocs=doc_ref.stream()
    name_lis=[]
    age_lis=[]
    documentId_lis=[]
    url_lis=[]
    for doc in alldocs:
        products=Product.from_dict(doc.to_dict())
        #print('{}=>{}' .format(doc.id,doc.to_dict(),doc.to_dict().name))
        name_lis.append(products.name)
        age_lis.append(products.price)
        documentId_lis.append(products.documentId)
        url_lis.append(products.downloadurl)
        # print(products.name)
        # print(products.age)
        # print(products.documentId)

    comb_lis=zip(name_lis,age_lis,documentId_lis,url_lis)
   
    return render(request,'hello.html',{'comb_lis':comb_lis})







def signIn(request):
    return render(request,"signIn.html")

def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid credentials"
        return render(request,"signIn.html",{"messg":message})
        #return redirect('/signIn/')
        #return render(request,"welcom.html",{"messg":message})
   # print(user['localId'])    
    uid=user['localId']

    session_id=user['idToken']

    #request.session['uid']=str(session_id)
    request.session['uid']=str(uid)
    

    
   


    user_ref=db.collection("users").document(uid)
    user_doc=user_ref.get()
    if user_doc.exists:
        usermodel=UserModel.from_dict(user_doc.to_dict())
        name=usermodel.name
        request.session['name']=name
    else:
        print(u'No such document!')
    return render(request,"home.html",{"uid":uid,'name':name})


def logout(request):
    #auth.logout(request)
    #authe.current_user = None
    request.session['uid']=None
    request.session['name']=None
   
    
    
    return render(request,'home.html')

def signUp(request):

    return render(request,"signUp.html")

    
def postsignup(request):
    # print("시작")
    email=request.POST.get('email')
    emailcheck=request.POST.get('emailcheck')
    password=request.POST.get('password')
    passwordre=request.POST.get('passwordre')
    checkbox=request.POST.get('checkbox')
    name=request.POST.get('name')

    # male=request.POST.get('male')
    # female=request.POST.get('female')
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
    uid={}
    if emailcheck=="인증":

        if len(password) >5 :
            if password==passwordre :
                try:
                    user=authe.create_user_with_email_and_password(email,password)
                    uid =user['localId']
                except:
                    msg="unalbe to create account try again"
                    return render(request,"signUp.html",{"msg":msg})
                
        else :
            msg="비밀번호를 6자리 이상 입력하시오"
            return render(request ,"signUp.html",{"msg":msg} )
            #return render(request,"home.html",{"msg":msg})
    else :
        msg="ID중복을 하시오"
        return render(request,"signUp.html",{"msg":msg})
    
    # print("유저 도큐 앞")
    user_doc_ref=db.collection("users").document(uid)
    # print("유저 도큐 뒤")
    #data={"name":name,"status":"1","uid":uid}

    user_doc_ref.set(
        UserModel(email,password,checkbox,name,sex,zipcode,adress,adressdetail,"","","","","").to_dict()
    )

    





    # doc_ref=db.collection('employee').document('empdoc')
    # doc_ref.set({
    #     'name':"양성열",
    #     '나이':"25"
    # })
    
    return render(request,"signIn.html")

    





# def create_admin(request):
#     Title=request.POST.get('Title')
#     Detail=request.POST.get('Detail')
#     url=request.POST.get('url')
    
#     #file=request.POST.get('file')

#     doc_ref=db.collection("product")
#     doc_ref_random=db.collection("product").document()
#     doc_ref_random.set(
#     Product(Title,Detail,doc_ref_random,url).to_dict()
#     )
    
#     return render(request,"create.html")

def detail(request,documentId):
    #테스트
    uid=None
    print("홈시작")
    try:
        recentview_lis=request.session['RecentView']
    except:
        print("recentview 없음")
    if len(recentview_lis)<6 :
        recentview_lis.append(documentId)
        my_set = set(recentview_lis)
        my_list = list(my_set)
        request.session['RecentView']=my_list
    else :
        recentview_lis.pop(0)
        recentview_lis.append(documentId)
        my_set = set(recentview_lis)
        my_list = list(my_set)
        request.session['RecentView']=my_list
    try:
        print("홈에서"+request.session['uid'])
        uid=request.session['uid']
    except:
        print("로그인안댐")
    doc_ref=db.collection(u'product').document(documentId)
    doc = doc_ref.get()
    products=None
    if doc.exists:
        print(u'Document data: {}'.format(doc.to_dict()))
        products=Product.from_dict(doc.to_dict())

    else:
        print(u'No such document!')

    
   

    return render(request,"detail.html",{'products':products,'documentId':documentId,'uid':uid})

def index(request):
    return render(request,"index.html")
def musinsa(request):
    return render(request,"dumex.html")


def top(request):
    #doc_ref=db.collection("product")
    uid=None
    try:
        # print("홈에서"+request.session['uid'])
        uid=request.session['uid']
    except:
         print("로그인안댐")

    doc_ref=db.collection(u'product').where(u"categori", u"==","상의")
    alldocs=doc_ref.stream()
    product_lis=[]

    for doc in alldocs:
        products=Product.from_dict(doc.to_dict())
        product_lis.append(products)


    #comb_lis=zip(name_lis,age_lis,documentId_lis,url_lis,categori_lis)
    
    return render(request ,'top.html',{"product_lis":product_lis,'uid':uid})

def bottom(request):
    uid=None
    try:
        print("홈에서"+request.session['uid'])
        uid=request.session['uid']
    except:
        print("로그인안댐")
     #doc_ref=db.collection("product")
    doc_ref=db.collection(u'product').where(u"categori", u"==",1)
    alldocs=doc_ref.stream()
    name_lis=[]
    age_lis=[]
    documentId_lis=[]
    url_lis=[]
    categori_lis=[]
    for doc in alldocs:
        products=Product.from_dict(doc.to_dict())
        #print('{}=>{}' .format(doc.id,doc.to_dict(),doc.to_dict().name))
        name_lis.append(products.name)
        age_lis.append(products.price)
        documentId_lis.append(products.documentId)
        url_lis.append(products.downloadurl)
        categori_lis.append(products.categori)
        # print(products.name)
        # print(products.age)
        # print(products.documentId)

    comb_lis=zip(name_lis,age_lis,documentId_lis,url_lis,categori_lis)
    

    return render(request ,'bottom.html',{"comb_lis":comb_lis,'uid':uid})

def bag(request):
    uid=None
    try:
        print("홈에서"+request.session['uid'])
        uid=request.session['uid']
    except:
        print("로그인안댐")
     #doc_ref=db.collection("product")
    doc_ref=db.collection(u'product').where(u"categori", u"==",2)
    alldocs=doc_ref.stream()
    name_lis=[]
    age_lis=[]
    documentId_lis=[]
    url_lis=[]
    categori_lis=[]
    for doc in alldocs:
        products=Product.from_dict(doc.to_dict())
        #print('{}=>{}' .format(doc.id,doc.to_dict(),doc.to_dict().name))
        name_lis.append(products.name)
        age_lis.append(products.price)
        documentId_lis.append(products.documentId)
        url_lis.append(products.downloadurl)
        categori_lis.append(products.categori)
        # print(products.name)
        # print(products.age)
        # print(products.documentId)

    comb_lis=zip(name_lis,age_lis,documentId_lis,url_lis,categori_lis)
    
    
    return render(request ,'bag.html',{"comb_lis":comb_lis,'uid':uid})

def etc(request):
    uid=None
    try:
        print("홈에서"+request.session['uid'])
        uid=request.session['uid']
    except:
        print("로그인안댐")
     #doc_ref=db.collection("product")
    doc_ref=db.collection(u'product').where(u"categori", u"==",3)
    alldocs=doc_ref.stream()
    name_lis=[]
    age_lis=[]
    documentId_lis=[]
    url_lis=[]
    categori_lis=[]
    for doc in alldocs:
        products=Product.from_dict(doc.to_dict())
        #print('{}=>{}' .format(doc.id,doc.to_dict(),doc.to_dict().name))
        name_lis.append(products.name)
        age_lis.append(products.price)
        documentId_lis.append(products.documentId)
        url_lis.append(products.downloadurl)
        categori_lis.append(products.categori)
        # print(products.name)
        # print(products.age)
        # print(products.documentId)

    comb_lis=zip(name_lis,age_lis,documentId_lis,url_lis,categori_lis)
    
    
    return render(request ,'etc.html',{"comb_lis":comb_lis,'uid':uid})

def pay(request):
    return render(request,'pay.html')
def thumbdetail(request):
    return render(request,'thumbdetail.html')
def cart(request):
    uid=None
    total_price=0
    total_amount=0;
    try:
        print("카트"+request.session['uid'])
        uid=request.session['uid']
        aldoc_ref=db.collection(u'users').document(uid).collection(u'cart')
        alldocs=aldoc_ref.stream()
        product_lis=[]
        option={}
        for doc in alldocs:
            cart=Cart.from_dict(doc.to_dict())
            product_lis.append(cart)
            total_price+=cart.totalprice
            total_amount+=cart.sizedic['s']+cart.sizedic['m']+cart.sizedic['l']+cart.sizedic['xl']
        inisisPrice=int(total_price)
        total_price =  format(inisisPrice, ',')
        
        return render(request, 'cart.html',{'product_lis':product_lis,'uid':uid,'total_price':total_price,'inisisPrice':inisisPrice})
    except:
        print("로그인안댐")
        return render(request, 'signIn.html')



def addcart(request):
    total_amount=0
    uid=None
    amount_s=""
    amount_m=""
    amount_l=""
    amount_xl=""
    amount_xxl=""
    try:
        print("카트"+request.session['uid'])
        uid=request.session['uid']
        products_name=request.POST.get('product_name')
        product_price=request.POST.get('product_price')
        product_id=request.POST.get('product_id')
        if request.POST.get('amount_S'):
            amount_s=request.POST.get('amount_S')
            print(amount_s)
        if request.POST.get('amount_M'):
            amount_m=request.POST.get('amount_M')
        if request.POST.get('amount_L'):
            amount_l=request.POST.get('amount_L')
        if request.POST.get('amount_XL'):
            amount_xl=request.POST.get('amount_XL')
        option={'s':0,'m':0,'l':0,'xl':0}

        if amount_s !='':
            option.update(s=int(amount_s))
            total_amount+=int(amount_s)
        if amount_m !='':
            option.update(m=int(amount_m))
            total_amount+=int(amount_m)
        if amount_l !='':
            option.update(l=int(amount_l))
            total_amount+=int(amount_l)
        if amount_xl !='':
            option.update(xl=int(amount_xl))
            total_amount+=int(amount_xl)
        
        #수량 선택이 안되었을때 파이썬편
        if total_amount <1 :
            return HttpResponseRedirect(request.POST['path'])


        
        doc_ref=db.collection(u'product').document(product_id)
        doc = doc_ref.get()
        products=None
        if doc.exists:
            products=Product.from_dict(doc.to_dict())
        else:
            print(u'No such document!')

        doc_ref2=db.collection(u'users').document(uid)
        doc2 = doc_ref2.get()
        usermodel=None
        if doc2.exists:
            print(u'Document data: {}'.format(doc2.to_dict()))
            usermodel=UserModel.from_dict(doc2.to_dict())
        else:
            print(u'No such document!')

        price3=""
        price=products.price.split('원')[0]
        price2=price.split(',')
        for a in price2:
            price3+=a
        total_price=int(price3)*total_amount
        print(format(int(total_price), ','))
        test=format(int(total_price), ',')
        
        if doc.exists and doc2.exists :
            doc_usercart=doc_ref2.collection(u'cart').document(products.documentId)
            doc_usercart.set(
                Cart(
                 products.name
                ,products.price
                ,products.documentId
                ,products.downloadurl
                ,products.categori
                ,products.brand
                ,option
                ,total_price
                ,total_amount
                ,format(int(total_price), ',')
                ).to_dict()
            )
            
        

        aldoc_ref=db.collection(u'users').document(uid).collection(u'cart')
        alldocs=aldoc_ref.stream()
        product_lis=[]
        ViewOption_lis=[]
        total_price=0
       
        for doc in alldocs:
            ViewOption=""
            cart=Cart.from_dict(doc.to_dict())
            print("카트포문")
            product_lis.append(cart)
            total_price+=cart.totalprice
            
            if cart.sizedic['s'] !=0:
                ViewOption+="S:"+str(cart.sizedic['s'])+"  "
            if cart.sizedic['m'] !=0:
                ViewOption+="M:"+str(cart.sizedic['m'])+"  "
            if cart.sizedic['l'] !=0:
                ViewOption+="L:"+str(cart.sizedic['l'])+"  "
            if cart.sizedic['xl'] !=0:
                ViewOption+="XL:"+str(cart.sizedic['xl'])+"  "

            ViewOption_lis.append(ViewOption)

        comb_lis=zip(product_lis,ViewOption_lis)
        inisisPrice=int(total_price)
        total_price =  format(inisisPrice, ',')
           
        return render(request, 'cart.html',{'comb_lis':comb_lis,'option':option,'uid':uid,'usermodel':usermodel,'total_price':total_price,'inisisPrice':inisisPrice})

    except:
        print("로그인안댐")
        return render(request, 'signIn.html')
  

def order(request):
   
    total_amount=0
    uid=None
    amount_s=""
    amount_m=""
    amount_l=""
    amount_xl=""
    amount_xxl=""

    try:
        print("오더"+request.session['uid'])
        uid=request.session['uid']
        products_name=request.POST.get('product_name')
        product_price=request.POST.get('product_price')
        product_id=request.POST.get('product_id')
        if request.POST.get('amount_S'):
            amount_s=request.POST.get('amount_S')
            print(amount_s)
        if request.POST.get('amount_M'):
            amount_m=request.POST.get('amount_M')
        if request.POST.get('amount_L'):
            amount_l=request.POST.get('amount_L')
        if request.POST.get('amount_XL'):
            amount_xl=request.POST.get('amount_XL')
        option={'s':0,'m':0,'l':0,'xl':0}
    #user=authe.currentUser
    #print(user)
        if amount_s !='':
            option.update(s=int(amount_s))
            total_amount+=int(amount_s)
        if amount_m !='':
            option.update(m=int(amount_m))
            total_amount+=int(amount_m)
        if amount_l !='':
            option.update(l=int(amount_l))
            total_amount+=int(amount_l)
        if amount_xl !='':
            option.update(xl=int(amount_xl))
            total_amount+=int(amount_xl)
        if amount_xxl !='':
            option.update(xl=int(amount_xl))
            total_amount+=int(amount_xl)
        print(amount_s)
        #print(int(amount_s))
        print(total_amount)
        #수량 선택이 안되었을때 파이썬편
        if total_amount <1 :
            return HttpResponseRedirect(request.POST['path'])
        
            

       
        doc_ref=db.collection(u'product').document(product_id)
        doc = doc_ref.get()
        products=None
        if doc.exists:
        #print(u'Document data: {}'.format(doc.to_dict()))
            products=Product.from_dict(doc.to_dict())
        else:
            print(u'No such document!')

        doc_ref2=db.collection(u'users').document(uid)
        doc2 = doc_ref2.get()
        usermodel=None
        if doc2.exists:
            print(u'Document data: {}'.format(doc2.to_dict()))
            usermodel=UserModel.from_dict(doc2.to_dict())
        else:
            print(u'No such document!')
        price3=""
        price=products.price.split('원')[0]
        price2=price.split(',')
        for a in price2:
            price3+=a
        

        #total_price=int(price3)*total_amount
     
        inisisPrice=int(price3)*total_amount
        total_price =  format(inisisPrice, ',')


        ##옵션 재 구성
        viewoption=""
        if option['s'] !=0:
            viewoption+="S:"+str(option['s'])+"  "
        if option['m'] !=0:
            viewoption+="M:"+str(option['m'])+"  "
        if option['l'] !=0:
            viewoption+="L:"+str(option['l'])+"  "
        if option['xl'] !=0:
            viewoption+="XL:"+str(option['xl'])+"  "
        return render(request, 'order.html',{'products':products,'option':viewoption,'uid':uid,'usermodel':usermodel,'total_amount':total_amount,'total_price':total_price,'inisisPrice':inisisPrice})

    except:
        expath=request.POST.get('path')
        print(expath)
        return render(request, 'order_login.html',{'expath':expath})
   




       

def kakaologin(request):
   

    client_id ='d63d18102aece9a328725d556a1fc114'
    #redirect_uri='http://127.0.0.1:8000/oauth/'
    redirect_uri='http://3.35.247.69/oauth/'

    access_token_request_uri="https://kauth.kakao.com/oauth/authorize?"
    access_token_request_uri+='client_id='+client_id
    access_token_request_uri+="&redirect_uri="+redirect_uri
    access_token_request_uri+="&response_type=code"
    print(access_token_request_uri)

    return redirect(access_token_request_uri)
def oauth(request):

    code=request.GET['code']
    print(code);
    
    client_id ='d63d18102aece9a328725d556a1fc114'
    #redirect_uri='http://127.0.0.1:8000/oauth/'
    redirect_uri='http://3.35.247.69/oauth/'

    access_token_request_uri="https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
    access_token_request_uri+='client_id='+client_id
    access_token_request_uri+="&redirect_uri="+redirect_uri
    access_token_request_uri+="&code="+code
    print(access_token_request_uri)
    access_token_request_uri_data=requests.get(access_token_request_uri)
    json_data=access_token_request_uri_data.json()
    access_token=json_data['access_token']
    print("accesstoken="+access_token)
    user_profile_info_uri="https://kapi.kakao.com/v2/user/me?access_token="
    user_profile_info_uri +=str(access_token)
    print("유저 딕션어리:"+user_profile_info_uri)
    user_profile_info_uri_data=requests.get(user_profile_info_uri)
    user_json_data=user_profile_info_uri_data.json()
    #이메일로그인
    #user_email=user_json_data['kakao_account']['email']
    user_id=user_json_data['id']
    user_email=str(user_id)+"@kakao.com"
    print(user_email)
    #전화번호 로그인
    user_nickname=user_json_data['properties']['nickname']
    password="kakaologin"
    ##이미 계정이 있을경우
    try: 
        user = auth.get_user_by_email(user_email)
        try:
            firebaseuser=authe.sign_in_with_email_and_password(user_email,password)
            uid =firebaseuser['localId']
            request.session['uid']=str(uid)

            user_ref=db.collection("users").document(uid)
            user_doc=user_ref.get()
            name=""
            if user_doc.exists:
                print(u'Document data: {}'.format(user_doc.to_dict()))
                usermodel=UserModel.from_dict(user_doc.to_dict())
                name=usermodel.name
            else:
                print(u'No such document!')


            
            return render(request,"home.html",{"uid":uid,'name':name})
            
        except:
            message="Invalid credentials"
            return render(request,"signIn.html",{"messg":message})
    ##처음 로그인 하는경우
    except :
        ##계정생성
        firebaseuser=authe.create_user_with_email_and_password(user_email,password)
        uid =firebaseuser['localId']
        request.session['uid']=str(uid)
        user_doc_ref=db.collection("users").document(uid)

        user_doc_ref.set(
            UserModel(user_email,password,"",user_nickname,"","","","","","","","","").to_dict()
        )

        try:
            firebaseuser=authe.sign_in_with_email_and_password(user_email,password)
            uid =firebaseuser['localId']


            user_ref=db.collection("users").document(uid)
            user_doc=user_ref.get()
            name=""
            if user_doc.exists:
                print(u'Document data: {}'.format(user_doc.to_dict()))
                usermodel=UserModel.from_dict(user_doc.to_dict())
                name=usermodel.name
            else:
                print(u'No such document!')

            return render(request,"home.html",{"uid":uid,'name':user_nickname})
        except:
            message="Invalid credentials"
            return render(request,"signIn.html",{"messg":message})

        
  
    #print('Successfully fetched user data: {0}'.format(user.uid))
    # result = auth.get_users([
    # auth.EmailIdentifier("ysy96pashon@naver.com")
    # ])
    # print('Successfully fetched user data:')
    # for user in result.users:
    #     print(user.uid)

    # print('Unable to find users corresponding to these identifiers:')
    # for uid in result.not_found:
    #     print(uid)

    
    return render(request, 'home.html',{'name':user_nickname})

def navercallback(request):
    NAVER_CLIENT_ID = 'gyHDnkTYKAXVqlUIyVLp'
    # NAVER_SECRET_KEY = 'aK3xMSwH14'

    code=request.GET['code']
    state=request.GET['state']
    print(code)
    req_info_info='https://nid.naver.com/oauth2.0/token?client_id='
    req_info_info+='gyHDnkTYKAXVqlUIyVLp'+'&client_secret='
    req_info_info+='aK3xMSwH14'+'&grant_type=authorization_code&state='
    req_info_info+=state+'&code='+code
    print(req_info_info)
    access_token_request_uri_data=requests.get(req_info_info)
    json_data=access_token_request_uri_data.json()
    print(json_data)
    accesstoken=json_data['access_token']
    print(accesstoken)
    user_profile_info_uri="https://openapi.naver.com/v1/nid/me?access_token="+accesstoken
    print(user_profile_info_uri)
    naverid=requests.get(user_profile_info_uri).json()['response']['id']
    print(naverid)

    user_email=str(naverid)+"@naver.com"
    print(user_email)
    #전화번호 로그인
    #user_nickname=user_json_data['properties']['nickname']
    user_nickname=None
    password="naverlogin"
    ##이미 계정이 있을경우
    try: 
        user = auth.get_user_by_email(user_email)
        try:
            firebaseuser=authe.sign_in_with_email_and_password(user_email,password)
            uid =firebaseuser['localId']
            request.session['uid']=str(uid)
            return render(request,"home.html",{"uid":uid})
            
        except:
            message="Invalid credentials"
            return render(request,"signIn.html",{"messg":message})
    ##처음 로그인 하는경우
    except :
        ##계정생성
        firebaseuser=authe.create_user_with_email_and_password(user_email,password)
        uid =firebaseuser['localId']
        request.session['uid']=str(uid)
        user_doc_ref=db.collection("users").document(uid)

        user_doc_ref.set(
            UserModel(user_email,password,"",user_nickname,"","","","","","","","","").to_dict()
        )

        try:
            firebaseuser=authe.sign_in_with_email_and_password(user_email,password)
            uid =firebaseuser['localId']
            return render(request,"home.html",{"uid":uid})
        except:
            message="Invalid credentials"
            return render(request,"signIn.html",{"messg":message})



 

    return render(request, 'home.html')

def googlelogin(request,uid):
    print("구글로그인"+uid)
    # print("구글이름"+name)
    request.session['uid']=uid

    user_doc_ref=db.collection("users").document(uid)
   

    doc = user_doc_ref.get()
    if doc.exists:
        print(u'Document data: {}'.format(doc.to_dict()))
    else:
        user_doc_ref.set(
        UserModel("","","","","","","","","","","","","").to_dict()
        )
        print(u'No such document!')

    


    return render(request,"home.html",{'uid':uid})

    

   
    


    
    
def check_email(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    passwordre=request.POST.get('passwordre')
    checkbox=request.POST.get('checkbox')
    name=request.POST.get('name')
    male=request.POST.get('male')
    female=request.POST.get('female')
    zipcode=request.POST.get('zipcode')
    adress=request.POST.get('adress')
    adressdetail=request.POST.get('adressdetail')
    adresscf=request.POST.get('adresscf')
    try:
        user = auth.get_user_by_email(email)
        msg="이미 아이디가 존재합니다"
        return render(request,'signUp.html',{'email':email,'password':password
        ,'checkbox':checkbox,'name':name,'male':male,'female':female
        ,'zipcode':zipcode,'adress':adress,'adressdetail':adressdetail,'adresscf':adresscf,'msg':msg})
    except:
        msg="사용할수있는 ID입니다"
        flag="인증"
        return render(request,'signUp.html',{'email':email,'password':password
        ,'checkbox':checkbox,'name':name,'male':male,'female':female
        ,'zipcode':zipcode,'adress':adress,'adressdetail':adressdetail,'adresscf':adresscf,'flag':flag,'msg':msg})


    
    
    
    # print(request.user.is_authenticated)
    # if uid != None :
    #     print("로그인")
def product_categoti(request , categori):
           #doc_ref=db.collection("product")
    uid=None
    try:
        # print("홈에서"+request.session['uid'])
        uid=request.session['uid']
    except:
        print("로그인안댐")

    doc_ref=db.collection(u'product').where(u"categori", u"==",categori)
    alldocs=doc_ref.stream()
    product_lis=[]

    for doc in alldocs:
        products=Product.from_dict(doc.to_dict())
        product_lis.append(products)
    return render(request ,'product.html',{"product_lis":product_lis,'uid':uid})

def cartdelete(request ,d_id) :
    print(d_id)
    uid=None
    try:
        # print("홈에서"+request.session['uid'])
        uid=request.session['uid']
        db.collection(u'users').document(uid).collection('cart').document(d_id).delete()


        
        aldoc_ref=db.collection(u'users').document(uid).collection(u'cart')
        alldocs=aldoc_ref.stream()
        product_lis=[]
        total_price=0
       
        for doc in alldocs:
            cart=Cart.from_dict(doc.to_dict())
            print("카트포문")
            product_lis.append(cart)
            total_price+=cart.totalprice
        inisisPrice=int(total_price)
        total_price =  format(inisisPrice, ',')

        aldoc_ref=db.collection(u'users').document(uid)

           
        return render(request, 'cart.html',{'product_lis':product_lis,'uid':uid,'total_price':total_price,'inisisPrice':inisisPrice})


    except:
        print("로그인안댐")
        return render(request,'signIn.html')

def cart_order(request):
   
    uid=None
    total_price=0
    total_amount=0;
    try:
        print("카트"+request.session['uid'])
        uid=request.session['uid']
        aldoc_ref=db.collection(u'users').document(uid).collection(u'cart')
        alldocs=aldoc_ref.stream()
        product_lis=[]
        ViewOption_lis=[]
        option={}
        for doc in alldocs:
            ViewOption=""
            cart=Cart.from_dict(doc.to_dict())
            product_lis.append(cart)
            total_price+=cart.totalprice
            total_amount+=cart.sizedic['s']+cart.sizedic['m']+cart.sizedic['l']+cart.sizedic['xl']
            ##옵션 리스트 만들기
            if cart.sizedic['s'] !=0:
                ViewOption+="S:"+str(cart.sizedic['s'])+"  "
            if cart.sizedic['m'] !=0:
                ViewOption+="M:"+str(cart.sizedic['m'])+"  "
            if cart.sizedic['l'] !=0:
                ViewOption+="L:"+str(cart.sizedic['l'])+"  "
            if cart.sizedic['xl'] !=0:
                ViewOption+="XL:"+str(cart.sizedic['xl'])+"  "
            ViewOption_lis.append(ViewOption)
        com_lis=zip(product_lis,ViewOption_lis)
        inisisPrice=int(total_price)
        total_price =  format(inisisPrice, ',')
        doc_ref=db.collection(u'users').document(uid)

        userdoc = doc_ref.get()
        products=None
        if userdoc.exists:
            userModel=UserModel.from_dict(userdoc.to_dict())
            print(u'유저모댈 data: {}'.format(userdoc.to_dict()))

        else:
            print(u'No such document!')

        
        return render(request, 'cart_order.html',{'com_lis':com_lis,'uid':uid,'total_price':total_price,'inisisPrice':inisisPrice,'usermodel':userModel})
    except:
        print("로그인안댐")
        return render(request, 'signIn.html')
def nonmember(request):
    expath=request.POST.get('path')

    print(expath)
    return render(request, 'nonmember_login.html',{'expath':expath})
def nonmember_create(request):

    expath=request.POST.get('path')
    name=request.POST.get('name')
    password=request.POST.get('pass')
    passwordre=request.POST.get('passre')
    tel=request.POST.get('tel')
    msg=""
    if password==passwordre :
        msg="비밀번호가 같다."
        request.session['uid']=tel
        return redirect(expath)
    else :
        msg="비밀번호 확인과 비밀번호가 일치하지 않습니다."
        return render(request, 'nonmember_login.html',{'msg':msg,'expath':expath})

  

    return render(request, 'home.html')

def order_postsign(request):
    expath=request.POST.get('path')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid credentials"
        return render(request,"signIn.html",{"messg":message})
        #return redirect('/signIn/')
        #return render(request,"welcom.html",{"messg":message})
   # print(user['localId'])    
    uid=user['localId']
    print("localId: "+uid)
    session_id=user['idToken']
    print("idtoken: "+session_id)
    #request.session['uid']=str(session_id)
    request.session['uid']=str(uid)
    print("포스트사인"+request.session['uid'])
    
    doc_ref=db.collection("product")
    alldocs=doc_ref.stream()
    name_lis=[]
    age_lis=[]
    documentId_lis=[]
    url_lis=[]
    for doc in alldocs:
        products=Product.from_dict(doc.to_dict())
        #print('{}=>{}' .format(doc.id,doc.to_dict(),doc.to_dict().name))
        name_lis.append(products.name)
        age_lis.append(products.price)
        documentId_lis.append(products.documentId)
        url_lis.append(products.downloadurl)
       # print(products.name)
       # print(products.age)
       # print(products.documentId)

    comb_lis=zip(name_lis,age_lis,documentId_lis,url_lis)
    #return render(request,"welcom.html",{"e":email})
    #return render(request,"home.html",{"uid":uid,"comb_lis":comb_lis})
    #return HttpResponse("OK")
    
    return redirect(expath)
def nonmember_lookup(request):
    
    return render(request,"nonmember_lookup.html")

def nonmember_lookup_action(request) :
    uid=None
    
    tel=request.POST.get('tel')
    uid=tel
    user_doc=db.collection("users").document(uid).collection("delivery")
    user_alldocs=user_doc.stream()
    print("??")
    deliverylist=[]
    for doc in user_alldocs:
        delivery=Delivery.from_dict(doc.to_dict())
        #print(delivery)
        deliverylist.append(delivery)
        
    return render(request, 'orderinfo.html',{'deliverylist':deliverylist})

def inbody(request):
    try:
        uid=request.session['uid']
        user_ref=db.collection("users").document(uid)
        
    except:
         return render(request, 'signin.html')
    

    return render(request, 'inbody.html')

def inbody_insert(request):
    height=request.POST.get('height')
    weight=request.POST.get('weight')
    SkeletalMuscleMass=request.POST.get('SkeletalMuscleMass')
    BodyFatMass=request.POST.get('BodyFatMass')
    BodyFatPercentage=request.POST.get('BodyFatPercentage')
    try:
        
        uid=request.session['uid']
        user_ref=db.collection("users").document(uid)
        user_ref.update({u'height': height})
        user_ref.update({u'weight': weight})
        user_ref.update({u'SkeletalMuscleMass': SkeletalMuscleMass})
        user_ref.update({u'BodyFatMass': BodyFatMass})
        user_ref.update({u'BodyFatPercentage': BodyFatPercentage})
     

    except:
         return render(request, 'signin.html')
    
          

    return render(request, 'home.html')

def review_write(request,delivery_uid):
    delivery_ref=db.collection("delivery").document(delivery_uid)
    delivery_doc=delivery_ref.get()
    if delivery_doc.exists:
        delivery=Delivery.from_dict(delivery_doc.to_dict())
        return render(request, 'reviewIndex.html',{"delivery_uid":delivery_uid,"delivery":delivery})
        

    else:
        print(u'No such document!')
    return render(request, 'reviewIndex.html',{"delivery_uid":delivery_uid})

def review_create(request,delivery_uid):

    try:

        uid=request.session['uid']
        user_doc=db.collection("users").document(uid).collection("delivery")
        user_alldocs=user_doc.stream()

        deliverylist=[]
        doc_id_lis=[]
        krtime_lis=[]
        option_lis=[]
        
        for doc in user_alldocs:

            option=""
            delivery=Delivery.from_dict(doc.to_dict())
            ustime=str(delivery.timestamp)[0:10]
            ##옵션 만들기
            
            if delivery.option['s'] !=0:
                option+="S:"+str(delivery.option['s'])+"  "
            if delivery.option['m'] !=0:
                option+="M:"+str(delivery.option['m'])+"  "
            if delivery.option['l'] !=0:
                option+="L:"+str(delivery.option['l'])+"  "
            if delivery.option['xl'] !=0:
                option+="XL:"+str(delivery.option['xl'])+"  "


            krtime_lis.append(ustime)
            deliverylist.append(delivery)
            doc_id_lis.append(doc.id)
            option_lis.append(option)
        
        comb_lis=zip(deliverylist,doc_id_lis,krtime_lis,option_lis)
        
        return render(request, 'orderinfo.html',{'uid':uid,'comb_lis':comb_lis})
    except:
        return render(request, 'signin.html',{'uid':uid})
    

    




  


    









