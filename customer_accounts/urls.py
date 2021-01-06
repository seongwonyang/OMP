from django.urls import re_path
from .splitviews import *

app_name = 'customer_accounts'

urlpatterns = [
    re_path(r'^login/$', LoginView, name='login'),
    re_path(r'^register/$', RegisterView, name='register'),
    re_path(r'^user-info/(?P<user_id>\d+)/$', InfoModifyView, name='info_modify'),
    re_path(r'^password/(?P<user_id>\d+)/$', PasswordModifyView, name='password_modify'),
    re_path(r'^logout/$', LogoutView, name='logout'),
    re_path(r'^user-info/$', InfoManageView, name='info_manage'),
    re_path(r'^password/$', PasswordCheckView, name='password_check'),
    re_path(r'^secede/$', UserDeleteView, name='user_delete'),
]