from django.db import models

# Create your models here.
class Product(object):

    def __init__(self
     ,name
     ,price
     ,documentId
     ,downloadurl
     ,categori
     ,brand
     ,detail_img_list
     ,detail_text
     ,timestamp
     ,fiexdPrice
     #1:top 2:bottom 3:bag 4:etc 
     ):
        self.name = name
        self.price=price
        self.documentId=documentId
        self.downloadurl=downloadurl
        self.categori=categori
        self.brand=brand
        self.detail_img_list=detail_img_list
        self.detail_text=detail_text
        self.timestamp=timestamp
        self.fiexdPrice=fiexdPrice
       
        

    @staticmethod
    def from_dict(source):
       
        product=Product(
         source[u'name']
        ,source[u'price']
        ,source[u'documentId']
        ,source[u'downloadurl']
        ,source[u'categori']
        ,source[u'brand']
        ,source[u'detail_img_list']
        ,source[u'detail_text']
        ,source[u'timestamp']
        ,source[u'fiexdPrice']
        )
        if u'name' in source:
            product.name = source[u'name']
        if u'price' in source:
            product.price = source[u'price']
        if u'documentId' in source:
            product.documentId = source[u'documentId']
        if u'downloadurl' in source:
            product.downloadurl = source[u'downloadurl']
        if u'categori' in source:
            product.categori = source[u'categori']
        if u'brand' in source:
            product.brand=source[u'brand']
        if u'detail_img_list' in source:
            product.detail_img_list=source[u'detail_img_list']
        if u'detail_text' in source:
            product.detail_text=source[u'detail_text']
        if u'timestamp' in source:
            product.timestamp=source[u'timestamp']
        if u'fiexdPrice' in source:
            product.fiexdPrice=source[u'fiexdPrice']
        
        return product
      

        
    def to_dict(self):
       
        dest = {
            u'name':self.name,
            u'price':self.price,
            u'documentId':self.documentId,
            u'downloadurl':self.downloadurl,
            u'categori':self.categori,
            u'brand':self.brand,
            u'detail_img_list':self.detail_img_list,
            u'detail_text':self.detail_text,
            u'timestamp':self.timestamp,
            u'fiexdPrice':self.fiexdPrice,
          
        }

        if self.name:
            dest[u'name'] = self.name

        if self.price:
            dest[u'price'] = self.price

        if self.documentId:
            dest[u'documentId'] = self.documentId
        
        if self.downloadurl:
            dest[u'downloadurl']=self.downloadurl

        if self.downloadurl:
            dest[u'categori']=self.categori

        if self.brand:
            dest[u'brand']=self.brand

        if self.detail_img_list:
            dest[u'detail_img_list']=self.detail_img_list
        if self.detail_text:
            dest[u'detail_text']=self.detail_text
        if self.timestamp:
                dest[u'timestamp']=self.timestamp
        if self.fiexdPrice:
                dest[u'fiexdPrice']=self.fiexdPrice

        return dest

    def __repr__(self):
        return(
             u'Product(name={}, price={})'
            .format(self.name
            ,self.price 
            ,self.documentId
            ,self.downloadurl
            ,self.categori
            ,self.brand
            ,self.detail_img_list
            ,self.detail_text
            ,self.timestamp
            ,self.fiexdPrice
            )
            )

class UserModel(object):

    def __init__(self
     ,email
     ,password 
     ,emailagree
     ,name
     ,sex
     ,zipcode
     ,adress
     ,adressdetail
     ): 
        self.email=email
        self.password=password
        self.emailagree=emailagree
        self.name=name
        self.sex=sex
        self.zipcode=zipcode
        self.adress=adress
        self.adressdetail=adressdetail
     
       
        

    @staticmethod
    def from_dict(source):
       
        usermodel=UserModel(
         source[u'email']
        ,source[u'password']
        ,source[u'emailagree']
        ,source[u'name']
        ,source[u'sex']
        ,source[u'zipcode']
        ,source[u'adress']
        ,source[u'adressdetail']
        )
        if u'email' in source:
            usermodel.email = source[u'email']
        if u'password' in source:
            usermodel.password = source[u'password']
        if u'emailagree' in source:
            usermodel.emailagree = source[u'emailagree']
        if u'name' in source:
            usermodel.name = source[u'name']
        if u'sex' in source:
            usermodel.sex = source[u'sex']
        if u'zipcode' in source:
            usermodel.zipcode = source[u'zipcode']
        if u'adress' in source:
            usermodel.adress = source[u'adress']
        if u'adressdetail' in source:
            usermodel.adressdetail = source[u'adressdetail']

       
        
        return usermodel
      

        
    def to_dict(self):
       
        dest = {
            u'email':self.email,
            u'password':self.password,
            u'emailagree':self.emailagree,
            u'name':self.name,
            u'sex':self.sex,
            u'zipcode':self.zipcode,
            u'adress':self.adress,
            u'adressdetail':self.adressdetail,
           
        }


        if self.email:
            dest[u'email'] = self.email

        if self.password:
            dest[u'password'] = self.password
        
        if self.emailagree:
            dest[u'emailagree']=self.emailagree
        
        if self.name:
            dest[u'name']=self.name

        if self.sex:
            dest[u'sex']=self.sex

        if self.zipcode:
            dest[u'zipcode']=self.zipcode

        if self.adress:
            dest[u'adress']=self.adress

        if self.adressdetail:
            dest[u'adressdetail']=self.adressdetail
        
        

       

        return dest

    def __repr__(self):
        return(
             u'UserModel(name={}, price={})'
            .format(
             self.email 
            ,self.password
            ,self.emailagree
            ,self.name
            ,self.sex
            ,self.zipcode
            ,self.adress
            ,self.adressdetail
           
            )
            )

class Cart(object):
    
    def __init__(self
     ,name
     ,price
     ,documentId
     ,downloadurl
     ,categori
     ,brand
     ,sizedic
     ,totalprice
     ,totalamount
     
     ):
        self.name = name
        self.price=price
        self.documentId=documentId
        self.downloadurl=downloadurl
        self.categori=categori
        self.brand=brand
        self.sizedic=sizedic
        self.totalprice=totalprice
        self.totalamount=totalamount

       
        

    @staticmethod
    def from_dict(source):
       
        cart=Cart(
         source[u'name']
        ,source[u'price']
        ,source[u'documentId']
        ,source[u'downloadurl']
        ,source[u'categori']
        ,source[u'brand']
        ,source[u'sizedic']
        ,source[u'totalprice']
        ,source[u'totalamount']
         )
        if u'name' in source:
            cart.name = source[u'name']
        if u'price' in source:
            cart.price = source[u'price']
        if u'documentId' in source:
            cart.documentId = source[u'documentId']
        if u'downloadurl' in source:
            cart.downloadurl = source[u'downloadurl']
        if u'categori' in source:
            cart.categori = source[u'categori']
        if u'brand' in source:
            cart.brand=source[u'brand']
        if u'sizedic' in source:
            cart.sizedic=source[u'sizedic']
        if u'totalprice' in source:
            cart.totalprice=source[u'totalprice']
        if u'totalamount' in source:
            cart.totalamount=source[u'totalamount']
        
        return cart
      

        
    def to_dict(self):
       
        dest = {
            u'name':self.name,
            u'price':self.price,
            u'documentId':self.documentId,
            u'downloadurl':self.downloadurl,
            u'categori':self.categori,
            u'brand':self.brand,
            u'sizedic':self.sizedic,
            u'totalprice':self.totalprice,
            u'totalamount':self.totalamount,
          
        }

        if self.name:
            dest[u'name'] = self.name

        if self.price:
            dest[u'price'] = self.price

        if self.documentId:
            dest[u'documentId'] = self.documentId
        
        if self.downloadurl:
            dest[u'downloadurl']=self.downloadurl

        if self.downloadurl:
            dest[u'categori']=self.categori

        if self.brand:
            dest[u'brand']=self.brand

        if self.sizedic:
            dest[u'sizedic']=self.sizedic

        if self.totalprice:
            dest[u'totalprice']=self.totalprice
        if self.totalamount:
            dest[u'totalamount']=self.totalamount

        return dest

    def __repr__(self):
        return(
             u'Product(name={}, price={})'
            .format(self.name
            ,self.price 
            ,self.documentId
            ,self.downloadurl
            ,self.categori
            ,self.brand
            ,self.sizedic
            ,self.totalprice
            ,self.totalamount
            )
            )
