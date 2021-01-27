from django.shortcuts import render
from myapp.views import db
from myapp.models import Product

# Create your views here.
def adminctr(request):

        return render(request,'adminctr.html')

def create(request):
    adminemail="hstore@admin.com"
    adminpass="123456789a"
    email=request.POST.get('email')
    passw=request.POST.get('pass')
#     try:
#             user=authe.sign_in_with_email_and_password(email,passw)
#     except:
#         message="Invalid credentials"
#         return render(request,"adminsite.html",{"messg":message})
#    # print(user['idToken'])    
#     session_id=user['idToken']
#     request.session['uid']=str(session_id)
    if adminemail != email or passw != adminpass  :
        message="Invalid credentials"
        return render(request,"adminctr.html",{"messg":message})
    return render(request,"create.html",{"e":email})
# def create(request):
#     print("크레이트실행")
#     return render(request,"create.html")

def create_admin(request):
    Title=request.POST.get('Title')
    Detail=request.POST.get('Detail')
    url=request.POST.get('url')
    categori=request.POST.get('categori')
    if not Title :
            messg="Title 입력하세요"
            return render(request ,'create.html',{"messg":messg})
    if not Detail :
            messg="Detail 입력하세요"
            return render(request ,'create.html',{"messg":messg})
    if not url :
            messg="url을 업로드 하세요"
            return render(request ,'create.html',{"messg":messg})
    if not categori :
            messg="categori 업로드 하세요"
            return render(request ,'create.html',{"messg":messg})


    
    #file=request.POST.get('file')

    doc_ref=db.collection("product")
    doc_ref_random=db.collection("product").document()
    doc_ref_random.set(
    Product(Title,Detail,doc_ref_random,url,categori).to_dict()
    )
    
    return render(request,"createadmin.html")
