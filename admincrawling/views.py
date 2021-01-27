from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
from firebase_admin import firestore
from myapp.models import Product
db=firestore.client()
def admincr(request):
    ##덤브스트럭
    # response= urlopen('https://dumbstruck.kr/product/list.html?cate_no=42')
    # soup=BeautifulSoup(response,'html.parser')
    # i=1
    # #print(soup.prettify())
    # # for anchor in soup.find_all("li", class_="item xans-record-"):
    # #     #print(str(i))
    # #     #print(anchor)
    # #     #print(str(i)+"위:" + anchor.get_text())
    # #     mystirng=anchor.get_text()[0:5]
    # #     print(mystirng)
    # #     i=i+1
    # # for anchor in soup.find_all("a", class_="thumb"):
    # #     imgURL = anchor.find("img")["src"]
    # #     #print(imgURL)
    # #     #print(str(i))
    # #     #print(anchor)
    # #     #print(str(i)+"위:" + anchor.get_text())
    # #     i=i+1
    # num=836
    # pdid="#anchorBoxId_"
    # for i in range(0,10):
    #     num=num-i
    #     thumbname=soup.select(pdid+str(num)+"> div.box > div.name > a > span")
    #     name=""
    #     price=""
    #     image=""
    #     categori=0
    #     brandnum="Thumb"+str(num)
    #     brand="Thumb"
       
    #     for a in thumbname:
    #         name=a.get_text()
    #         print(name)
    #     thumbprice=soup.select(pdid+str(num)+"> div.box > div.xans-element-.xans-product.xans-product-listitem.table > div > span:nth-child(1)")
    #     for b in thumbprice:
    #         price=b.get_text()
    #         print(price)
    #     #thumbimg=soup.select(pdid+str(num)+"> div:nth-child(1) > a > img")
    #     thumbimg=soup.select(pdid+str(num)+"> div:nth-child(1) > a ")
    #     for c in thumbimg:
    #         image=c.find("img")["src"]
    #         print(image)
    #     doc_ref=db.collection("product")
    #     doc_ref_random=db.collection("product").document(brandnum)
    #     doc_ref_random.set(
    #     Product(name,price,doc_ref_random,image,categori,brand).to_dict()
    #     )
    # ##피투씨
    # response2= urlopen('https://fit2c.com/category/dryfit/54/')
    # soup2=BeautifulSoup(response2,'html.parser')
    # i=1
    # #print(soup.prettify())
    # # for anchor in soup.find_all("li", class_="item xans-record-"):
    # #     #print(str(i))
    # #     #print(anchor)
    # #     #print(str(i)+"위:" + anchor.get_text())
    # #     mystirng=anchor.get_text()[0:5]
    # #     print(mystirng)
    # #     i=i+1
    # # for anchor in soup.find_all("a", class_="thumb"):
    # #     imgURL = anchor.find("img")["src"]
    # #     #print(imgURL)
    # #     #print(str(i))
    # #     #print(anchor)
    # #     #print(str(i)+"위:" + anchor.get_text())
    # #     i=i+1
    # num=375
    # pdid="#anchorBoxId_"
    # for i in range(0,3):
    #     num=num-i
    #     #anchorBoxId_375 
    #     PTOCname=soup2.select(pdid+str(num)+"> div > p.name > a > span")
    #     name=""
    #     price=""
    #     image=""
    #     categori=0
    #     brandnum="PTOC"+str(num)
    #     brand="PTOC"
    #     for a in PTOCname:
    #         name=a.get_text()
    #         print(name)
    #         #anchorBoxId_375 

    #     PTOCprice=soup2.select(pdid+str(num)+"> div > p.price")
    #     for b in PTOCprice:
    #         price=b.get_text()
    #         print(price)
    #     #thumbimg=soup.select(pdid+str(num)+"> div:nth-child(1) > a > img")

    #     PTOCimg=soup2.select(pdid+str(num)+"> div > a")
    #     for c in PTOCimg:
    #         image=c.find("img")["src"]
    #         print(image)
    #     doc_ref=db.collection("product")
    #     doc_ref_random=db.collection("product").document(brandnum)
    #     doc_ref_random.set(
    #     Product(name,price,doc_ref_random,image,categori,brand).to_dict()
    #     )
    return render(request,'admincr.html')

def crawling(request):

    crawl_url=request.POST.get('crawl_url')
    crawl_brand=request.POST.get('crawl_brand')
    crawl_number=request.POST.get('crawl_number')
    crawl_selectname=request.POST.get('crawl_selectname')
    crawl_selectprice=request.POST.get('crawl_price')
    crawl_selectimage=request.POST.get('crawl_image')
    categori=request.POST.get('categori')

    
   
    response= urlopen(crawl_url)
    soup=BeautifulSoup(response,'html.parser')
    i=1
    


    
    name=""
    price=""
    image=""
  
    brandnum=crawl_brand+str(crawl_number)
    

    cr_name=soup.select(crawl_selectname)
    for a in cr_name:
        name=a.get_text()
        print(name)
      

    cr_price=soup.select(crawl_selectprice)
    for b in cr_price:
        price=b.get_text()
        print(price)
        #thumbimg=soup.select(pdid+str(num)+"> div:nth-child(1) > a > img")

    cr_img=soup.select(crawl_selectimage)
    for c in cr_img:
        image=c.find("img")["src"]
        print(image)
    
    if name == None :
        msg="nameselect  공백이다"
        return render(request,'crawling.html',{'msg':msg})
    elif price == None :
        msg="가격  공백이다"
        return render(request,'crawling.html',{'msg':msg})
    elif image == None :
        msg="이미지  공백이다"
        return render(request,'crawling.html',{'msg':msg})
    else:
        doc_ref=db.collection("product")
        doc_ref_random=db.collection("product").document(brandnum)
        doc_ref_random.set(
        Product(name,price,brandnum,image,categori,crawl_brand).to_dict()
        )
        msg="업로드 성공적"
        return render(request,'crawling.html',{'msg':msg})
    
    
   
    