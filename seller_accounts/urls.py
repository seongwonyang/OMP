from django.urls import re_path
from .splitviews import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'seller_accounts'

urlpatterns = [
    re_path(r'^seller_register/$', SellerRegisterView, name='seller_register'),
    re_path(r'^bookstore_register/$', BookStoreRegisterView, name='bookstore_register'),
    re_path(r'^shipping_info_register/$', ShippingInfoRegisterView, name='shipping_info_register'),
    re_path(r'^seller_login/$', SellerLoginView, name='seller_login'),
    re_path(r'^seller_info/$', SellerInfoView, name='seller_info'),
    re_path(r'^seller_info/bookstore/(?P<user_id>\d+)/$', BookstoreModifyView, name='bookstore_modify'),
    re_path(r'^seller_info/shipping_info/$', ShippingInfoModifyView, name='shipping_info_modify'),
    re_path(r'^secede/$', SellerDeleteView, name='seller_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)