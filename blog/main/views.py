from django.shortcuts import render, redirect
from main.models import Post
from datetime import datetime
from markdown2 import Markdown

def splash_view(request):
    posts = Post.objects.order_by('-time')
    return render(request, "splash.html", {'posts': posts})

def post_view(request):
    # if the post id does not exist, redirect to the splash page
    if not Post.objects.filter(post_id=request.GET['id']).exists():
        return redirect('/')
    post = Post.objects.get(post_id = request.GET['id'])
    md = Markdown()
    post.content = md.convert(post.content)
    return render(request, 'post.html', {"post": post})
