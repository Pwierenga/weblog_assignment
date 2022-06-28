import imp
from math import fabs
from pickle import FALSE
from queue import Empty
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Reaction
from .forms import PostForm, ReactionForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
  return render(request, 'blog/home.html', {})

def posts(request):
  posts = Post.objects.all()
  if request.user in User.objects.all():
    can_post = True
  else:
    can_post = False
  return render(request, 'blog/posts.html', {'posts': posts, 'can_post': can_post })

def post_detail(request, pk):
  if request.method == 'POST':
    form = ReactionForm(request.POST)
    reaction = form.save(commit=False)
    reaction.post_id = pk
    if not reaction.author:
      reaction.author = 'Anoniem' 
    reaction.save()    
  
  post = get_object_or_404(Post, pk=pk)
  form = ReactionForm()
  reactions = list(Reaction.objects.filter(post_id=pk))
  return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'reactions': reactions})

def new_post(request):
  if not request.user in User.objects.all():
    return render(request, 'blog/home.html', {})
  
  if request.method == 'POST':
    form = PostForm(request.POST)
    post = form.save(commit=False)
    if form.is_valid():
      
      if request.user in User.objects.all():
        post.author = request.user
        
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    form = PostForm()
  return render(request, 'blog/new_post.html', {'form': form})

def users(request):
  return render(request, 'blog/users.html', {'users': User.objects.all()})
