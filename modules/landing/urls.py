from django.conf.urls import url
from .views import index,signup,login,logout,uploadImage

urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^signup/$', signup,name="sign"),
    url(r'^login/$', login,name="login"),
    url(r'^logout/$', logout,name="logout"),
    url(r'^new/image/$', uploadImage,name="uploadImage"),
]
