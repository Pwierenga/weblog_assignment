from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('posts', views.posts, name = 'posts'),
  path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
  path('new_post', views.new_post, name = 'new_post'),
  path('users', views.users, name = 'users')
  
]