
from django.urls import path

from repo import views

urlpatterns = [
    path('', views.home,name='home'),
    # path('home', views.home,name='home'),
    # path('detail', views.detail,name='detail'),
]
