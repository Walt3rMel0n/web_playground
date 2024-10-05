from django.urls import path
from . import views
from .views import BlogCreate


blog_patterns = ([
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
    path('create/', BlogCreate.as_view(), name="create"),

], 'blogs')