
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import myapp.views
import address.views
import adminctr.views
import admincrawling.views
import mypage.views
import delivery.views



urlpatterns = [
    path('adminctr/', adminctr.views.adminctr,name="adminctr"),
    path('adminctr/create/', adminctr.views.create,name="create"),
    #path('adminsite/', adminctr.views.adminsite,name="adminsite"),
    path('', myapp.views.home,name="home"),
    #path('', myapp.views.index,name="index"),
    #path('', myapp.views.musinsa,name="musinsa"),
    path('hello/', myapp.views.hello,name="hello"),
    path('signIn/', myapp.views.signIn,name="signIn"),
    path('postsign/', myapp.views.postsign,name="postsign"),
    path('logout/', myapp.views.logout,name="logout"),
    path('signUp/', myapp.views.signUp,name="signUp"),
    path('postsignup/', myapp.views.postsignup,name="postsignup"),
#   path('postsign_admin/', adminctr.views.postsign_admin,name="postsign_admin"),
   
    path('create_admin/', adminctr.views.create_admin,name="create_admin"),
    #path('detail/', myapp.views.detail,name="detail"),
    path('detail/<str:documentId>', myapp.views.detail, name="detail" ) ,
    path('addressserch/',address.views.test,name="addressserch"),
    path('product/<str:categori>',myapp.views.product_categoti,name="product_categoti"),
    # path('top/',myapp.views.top,name="top"),
    # path('bottom/',myapp.views.bottom,name="bottom"),
    # path('bag/',myapp.views.bag,name="bag"),
    # path('etc/',myapp.views.etc,name="etc"),
    path('pay/',myapp.views.pay,name="pay"),
    #path('admincr/',admincrawling.views.admincr,name="admincr"),
    path('crawling/',admincrawling.views.crawling,name="crawling"),
    path('thumbdetail/',myapp.views.thumbdetail,name="thumbdetail"),
    path('addcart/', myapp.views.addcart,name="addcart"),
    path('order/', myapp.views.order,name="order"),
    path('mypage/', mypage.views.mypage,name="mypage"),
    path('orderinfo/', mypage.views.orderinfo,name="orderinfo"),
    path('cart/', myapp.views.cart,name="cart"),
    path('kakaologin/', myapp.views.kakaologin,name="kakaologin"),
    path('oauth/', myapp.views.oauth,name="oauth"),
    path('naver/callback/', myapp.views.navercallback,name="navercallback"),
    #path('google/<str:uid>/<str:name>/', myapp.views.googlelogin, name="googlelogin" ) ,
    path('google/<str:uid>/', myapp.views.googlelogin, name="googlelogin" ) ,
    path('signup/check_email/', myapp.views.check_email, name="check_email" ) ,
    path('cart/delete/<str:d_id>', myapp.views.cartdelete,name="cartdelete"),
    path('delivery/', delivery.views.index,name="cartdelete"),
   
    path('delivery/getdata', delivery.views.getdata,name="getdata"),
    path('cart/order/', myapp.views.cart_order,name="cart_order"),
    path('order/complete/<str:brandname>/<str:product_name>/<str:option>/<int:price>/<str:username>/<int:phonenum>/<str:address>/<str:uid>/<str:delivery_message>/', delivery.views.getdata,name="complete"),
    path('cart/order/complete/<int:total_price>/<str:username>/<int:phonenumber>/<str:address>/<str:uid>/<str:delivery_message>/', delivery.views.cart_order_complete,name="cart_order_complete"),
   

   
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
