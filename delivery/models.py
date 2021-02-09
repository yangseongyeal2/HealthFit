from django.db import models

class Delivery(object):
    
    def __init__(self
     ,brandname
     ,product_name
     ,option
     ,price
     ,username
     ,phonenum
     ,address
     ,timestamp
     ,deliverystate
     ,deliverynum
     ,deliverycode
     ,uid
     ,delivery_message
     ,img
     ,product_id
     
     ):
        self.brandname = brandname
        self.product_name=product_name
        self.option=option
        self.price=price
        self.username=username
        self.phonenum=phonenum
        self.address=address
        self.timestamp=timestamp
        self.deliverystate=deliverystate
        self.deliverynum=deliverynum
        self.deliverycode=deliverycode
        self.uid=uid
        self.delivery_message=delivery_message
        self.img=img
        self.product_id=product_id

       
        

    @staticmethod
    def from_dict(source):
       
        delivery=Delivery(
         source[u'brandname']
        ,source[u'product_name']
        ,source[u'option']
        ,source[u'price']
        ,source[u'username']
        ,source[u'phonenum']
        ,source[u'address']
        ,source[u'timestamp']
        ,source[u'deliverystate']
        ,source[u'deliverynum']
        ,source[u'deliverycode']
        ,source[u'uid']
        ,source[u'delivery_message']
        ,source[u'img']
        ,source[u'product_id']
         )
        if u'brandname' in source:
            delivery.brandname = source[u'brandname']
        if u'product_name' in source:
            delivery.product_name = source[u'product_name']
        if u'option' in source:
            delivery.option = source[u'option']
        if u'price' in source:
            delivery.price = source[u'price']
        if u'username' in source:
            delivery.username = source[u'username']
        if u'phonenum' in source:
            delivery.phonenum = source[u'phonenum']
        if u'address' in source:
            delivery.address=source[u'address']
        if u'timestamp' in source:
            delivery.timestamp=source[u'timestamp']
        if u'deliverystate' in source:
            delivery.deliverystate=source[u'deliverystate']
        if u'deliverynum' in source:
            delivery.deliverynum=source[u'deliverynum']
        if u'deliverycode' in source:
            delivery.deliverycode=source[u'deliverycode']
        if u'uid' in source:
            delivery.uid=source[u'uid']
        if u'img' in source:
            delivery.img=source[u'img']
        if u'delivery_message' in source:
            delivery.delivery_message=source[u'delivery_message']
        if u'product_id' in source:
            delivery.product_id=source[u'product_id']
        
        return delivery
      

        
    def to_dict(self):
       
        dest = {
            u'brandname':self.brandname,
            u'product_name':self.product_name,
            u'option':self.option,
            u'price':self.price,
            u'username':self.username,
            u'phonenum':self.phonenum,
            u'address':self.address,
            u'timestamp':self.timestamp,
            u'deliverystate':self.deliverystate,
            u'deliverynum':self.deliverynum,
            u'deliverycode':self.deliverycode,
            u'uid':self.uid,
            u'delivery_message':self.delivery_message,
            u'img':self.img,
            u'product_id':self.product_id,
          
        }

        if self.brandname:
            dest[u'brandname'] = self.brandname

        if self.product_name:
            dest[u'product_name'] = self.product_name

        if self.option:
            dest[u'option'] = self.option
        
        if self.price:
            dest[u'price']=self.price

        if self.username:
            dest[u'username']=self.username

        if self.phonenum:
            dest[u'phonenum']=self.phonenum

        if self.address:
            dest[u'address']=self.address

        if self.timestamp:
            dest[u'timestamp']=self.timestamp

        if self.deliverystate:
            dest[u'deliverystate']=self.deliverystate
        if self.deliverynum:
            dest[u'deliverynum']=self.deliverynum
        if self.deliverycode:
            dest[u'deliverycode']=self.deliverycode
        if self.uid:
            dest[u'uid']=self.uid
        if self.delivery_message:
            dest[u'delivery_message']=self.delivery_message
        if self.img:
            dest[u'img']=self.img
        if self.product_id:
            dest[u'product_id']=self.product_id

        return dest

    def __repr__(self):
        return(
             u'Delivery(name={}, price={})'
            .format(self.brandname
            ,self.product_name 
            ,self.option
            ,self.price
            ,self.username
            ,self.phonenum
            ,self.address
            ,self.timestamp
            ,self.deliverystate
            ,self.deliverynum
            ,self.deliverycode
            ,self.uid
            ,self.delivery_message
            ,self.img
            ,self.product_id
            )
            )

