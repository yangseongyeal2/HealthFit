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
#     Title=request.POST.get('Title')
#     Detail=request.POST.get('Detail')
#     url=request.POST.get('url')
#     categori=request.POST.get('categori')
#     if not Title :
#             messg="Title 입력하세요"
#             return render(request ,'create.html',{"messg":messg})
#     if not Detail :
#             messg="Detail 입력하세요"
#             return render(request ,'create.html',{"messg":messg})
#     if not url :
#             messg="url을 업로드 하세요"
#             return render(request ,'create.html',{"messg":messg})
#     if not categori :
#             messg="categori 업로드 하세요"
#             return render(request ,'create.html',{"messg":messg})
    
    adminBrandNumber=request.POST.get('adminBrandNumber')
    print("브랜드넘버:"+adminBrandNumber)
    adminBrandName=request.POST.get('adminBrandName')
    print("브랜드이름:"+adminBrandName)
    adminProductCategory=request.POST.get('adminProductCategory')
    print("카테고리:"+adminProductCategory)
    adminProductName=request.POST.get('adminProductName')
    print("상품이름:"+adminProductName)
    adminProductPrice=request.POST.get('adminProductPrice')
    print("가격:"+adminProductPrice)
    adminProuctMaimImage=request.POST.get('adminProuctMaimImage')
    print("메인이미지:"+adminProuctMaimImage)

    cnt=request.POST.get('cnt')
    print("카운트:"+cnt)
    cnt=int(cnt)
    lis_detail_img=[]
    if cnt !=None :
        for count in range(1,cnt+1):
                adminProuctDetailImageCnt="adminProuctDetailImage"+str(count)
                print("count:"+adminProuctDetailImageCnt)
                img=request.POST.get(adminProuctDetailImageCnt)
                print("가져온 이미지:"+img)
                lis_detail_img.append(img)

    adminDetailText=request.POST.get('adminDetailText')
    print("상세텍스트:"+adminDetailText)


   




    documentId=adminBrandName+adminBrandNumber
    #file=request.POST.get('file')
    doc_ref=db.collection("product")
    doc_ref_random=db.collection("product").document(documentId)
    doc_ref_random.set(
    Product(
            adminProductName
            ,adminProductPrice
            ,documentId
            ,adminProuctMaimImage
            ,adminProductCategory
            ,adminBrandName
            ,lis_detail_img
            ,adminDetailText
            ).to_dict())
    
    return render(request,"createadmin.html")


def adminProductManager(request):
    return render(request,"productmanager.html")
