from django.contrib import admin
from django.urls import path,include,re_path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('bloghome/',views.bloghome,name='bloghome'),
    path('blogpost/', views.blogpost, name='blogpost'), 
    path('blogsearch/', views.blogsearch, name='blogsearch'), 
    path('blogread/<str:slug>', views.blogread, name='blogread'), 
    # API to Post Comment 
    path('postcomment/',views.postcomment,name='postcomment')
]

# <str:slug_text>