from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})

def create(request):
    # Add Post
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('detail', post.id)

    # Show Crete Form
    else: # request.method == 'GET'
        return render(request, 'create.html')

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # Edit Post
    if request.method == 'POST':
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('detail', post.id) 

    # Show Update Form
    else:
        return render(request, 'update.html', {'post': post})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home')

def signup(request):
    # Signup Form을 누가 제출했을 때
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        return redirect('home')
    # Show Signup Form
    return render(request, 'signup.html')