from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
# class Order(models.Model):
#     first_name=models.CharField(max_length=50)
#     last_name=models.CharField(max_length=50)
#     email=models.EmailField()
#     address=models.CharField(max_length=250)
#     postal_code=models.CharField(max_length=250)
#     city=models.CharField(max_length=100)
#     created=models.DateTimeField(auto_now_add=True)
#     updated=models.DateTimeField(auto_now=True)
#     paid=models.BooleanField(default=False)
    
#     #coupon=models.ForeignKey(Coupon,on_delete=models.PROTECT,related_name='order_coupon',null=True,blank=True)
#     discount=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(100000)])

#         class Meta:
#             ordering=['-created']
        
#         def __str__(self):
#             return f'Order {self.id}'
        
#         def get_total_product(self):
#             return sum(item.get_item_price() for item in self.items.all())
#         def get_total_price(self):
#             total_product=self.get_total_price_product()
#             return total_product-self.discount
        
