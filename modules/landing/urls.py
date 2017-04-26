from django.conf.urls import url
from .views import index,signup,login,logout

urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^signup/$', signup,name="sign"),
    url(r'^login/$', login,name="login"),
    url(r'^logout/$', logout,name="logout"),
]
