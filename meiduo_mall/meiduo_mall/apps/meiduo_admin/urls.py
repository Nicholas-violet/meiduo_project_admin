
from django.urls import re_path
from meiduo_admin.views.login_views import *

urlpatterns = [
    re_path(r'^authorizations/$', LoginAPIView.as_view()),
]