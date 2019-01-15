from django.conf.urls import url, include
from .views import index, index_template, user_login

urlpatterns = [
    url(r'^hello/', index),
    url(r'^hellot/', index_template),
    url(r'^user_login/', user_login)
]
