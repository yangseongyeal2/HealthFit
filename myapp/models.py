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
     ,height
     ,weight
     ,SkeletalMuscleMass
     ,BodyFatMass
     ,BodyFatPercentage
     ): 
        self.email=email
        self.password=password
        self.emailagree=emailagree
        self.name=name
        self.sex=sex
        self.zipcode=zipcode
        self.adress=adress
        self.adressdetail=adressdetail
        self.height=height
        self.weight=weight
        self.SkeletalMuscleMass=SkeletalMuscleMass
        self.BodyFatMass=BodyFatMass
        self.BodyFatPercentage=BodyFatPercentage
     
       
        

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
        ,source[u'height']
        ,source[u'weight']
        ,source[u'SkeletalMuscleMass']
        ,source[u'BodyFatMass']
        ,source[u'BodyFatPercentage']
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
        if u'height' in source:
            usermodel.height = source[u'height']

        if u'weight' in source:
            usermodel.weight = source[u'weight']

        if u'SkeletalMuscleMass' in source:
            usermodel.SkeletalMuscleMass = source[u'SkeletalMuscleMass']

        if u'BodyFatMass' in source:
            usermodel.BodyFatMass = source[u'BodyFatMass']

        if u'BodyFatPercentage' in source:
            usermodel.BodyFatPercentage = source[u'BodyFatPercentage']


       
        
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

            u'height':self.height,
            u'weight':self.weight,
            u'SkeletalMuscleMass':self.SkeletalMuscleMass,
            u'BodyFatMass':self.BodyFatMass,
            u'BodyFatPercentage':self.BodyFatPercentage,
           
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
        if self.height:
            dest[u'height']=self.height
        if self.weight:
            dest[u'weight']=self.weight
        if self.SkeletalMuscleMass:
            dest[u'SkeletalMuscleMass']=self.SkeletalMuscleMass
        if self.BodyFatMass:
            dest[u'BodyFatMass']=self.BodyFatMass
        if self.BodyFatPercentage:
            dest[u'BodyFatPercentage']=self.BodyFatPercentage
        
        

       

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
            ,self.height
            ,self.weight
            ,self.SkeletalMuscleMass
            ,self.BodyFatMass
            ,self.BodyFatPercentage
           
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
     ,fixedPrice
     
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
        self.fixedPrice=fixedPrice

       
        

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
        ,source[u'fixedPrice']
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
        if u'fixedPrice' in source:
            cart.fixedPrice=source[u'fixedPrice']
        
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
            u'fixedPrice':self.fixedPrice,
          
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
        if self.fixedPrice:
            dest[u'fixedPrice']=self.fixedPrice

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
            ,self.fixedPrice
            )
            )

class Review(object):
    
    def __init__(self
     ,StarPoint
     ,user_uid
     ,delivery_uid
     ,text
     ,SizePoint
     ,BrightPoint
     ,ColorPoint
     ,ThickPoint
     ,timestamp
     
    
     ):
        self.StarPoint = StarPoint
        self.user_uid=user_uid
        self.delivery_uid=delivery_uid
        self.text=text
        self.SizePoint=SizePoint
        self.BrightPoint=BrightPoint
        self.ColorPoint=ColorPoint
        self.ThickPoint=ThickPoint
        self.timestamp=timestamp
       
       
        

    @staticmethod
    def from_dict(source):
       
        review=Review(
         source[u'StarPoint']
        ,source[u'user_uid']
        ,source[u'delivery_uid']
        ,source[u'text']
        ,source[u'SizePoint']
        ,source[u'BrightPoint']
        ,source[u'ColorPoint']
        ,source[u'ThickPoint']
        ,source[u'timestamp']
     
        )
        if u'StarPoint' in source:
            review.StarPoint = source[u'StarPoint']
        if u'user_uid' in source:
            review.user_uid = source[u'user_uid']
        if u'delivery_uid' in source:
            review.delivery_uid = source[u'delivery_uid']
        if u'text' in source:
            review.text = source[u'text']
        if u'SizePoint' in source:
            review.SizePoint = source[u'SizePoint']
        if u'BrightPoint' in source:
            review.BrightPoint=source[u'BrightPoint']
        if u'ColorPoint' in source:
            review.ColorPoint=source[u'ColorPoint']
        if u'ThickPoint' in source:
            review.ThickPoint=source[u'ThickPoint']
        if u'timestamp' in source:
            review.timestamp=source[u'timestamp']
     
        
        return review
      

        
    def to_dict(self):
       
        dest = {
            u'StarPoint':self.StarPoint,
            u'user_uid':self.user_uid,
            u'delivery_uid':self.delivery_uid,
            u'text':self.text,
            u'SizePoint':self.SizePoint,
            u'BrightPoint':self.BrightPoint,
            u'ColorPoint':self.ColorPoint,
            u'ThickPoint':self.ThickPoint,
            u'timestamp':self.timestamp,
           
          
        }

        if self.StarPoint:
            dest[u'StarPoint'] = self.StarPoint

        if self.user_uid:
            dest[u'user_uid'] = self.user_uid

        if self.delivery_uid:
            dest[u'delivery_uid'] = self.delivery_uid
        
        if self.text:
            dest[u'text']=self.text

        if self.SizePoint:
            dest[u'SizePoint']=self.SizePoint

        if self.BrightPoint:
            dest[u'BrightPoint']=self.BrightPoint

        if self.ColorPoint:
            dest[u'ColorPoint']=self.ColorPoint
        if self.ThickPoint:
            dest[u'ThickPoint']=self.ThickPoint
        if self.timestamp:
                dest[u'timestamp']=self.timestamp
    

        return dest

    def __repr__(self):
        return(
             u'Review(name={}, price={})'
            .format(
            self.StarPoint
            ,self.user_uid 
            ,self.delivery_uid
            ,self.text
            ,self.SizePoint
            ,self.BrightPoint
            ,self.ColorPoint
            ,self.ThickPoint
            ,self.timestamp
        
            )
            )
