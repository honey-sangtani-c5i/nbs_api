from django.conf.urls import url 
from api import views 
 
urlpatterns = [ 
    url(r'^api/getUser$', views.getUser),
]