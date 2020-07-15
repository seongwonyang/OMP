from django.urls import re_path
from .splitviews import *

app_name = 'customer'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
    re_path(r'^search_store/$', SearchStoreView, name='search_store'),
    re_path(r'^searchBook/$', SearchBookView, name='search_book'),
    re_path(r'^searchBookResult/$', SearchBookResultView, name='search_book_result'),
    re_path(r'^mypage/$', MypageView, name='mypage'),
    re_path(r'^ajax_get_city/$', AjaxGetCityView, name='ajax_get_city'),
]
