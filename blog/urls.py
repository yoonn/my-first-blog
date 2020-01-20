from django.urls import path
from . import views

urlpatterns = [
    # root url 설정
    path('', views.post_list, name='post_list'),
]