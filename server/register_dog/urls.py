from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'register_dog'

urlpatterns = [
    path('', views.main1, name='main1'),
    path('main2/', views.main2, name='main2'),
    path('create_post_lost/', views.LostCreate.as_view(), name="create_post_lost"),
    path('create_post_found/', views.FoundCreate.as_view(), name="create_post_found"),
    path('mypage/', views.mypage, name="mypage"),
]