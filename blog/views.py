from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required



# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})

@method_decorator(login_required, name='dispatch')    
class BlogCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'published', 'author', 'image', 'categories']
    success_url = reverse_lazy('blogs:blog')