from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path('', views.postslist.as_view(), name='posts'),
    path('add-post/', views.add_post, name="add_post"),
    path('<slug:slug>/', views.postdetail.as_view(), name='post_detail'),
]
