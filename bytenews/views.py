from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'bytenews/home.html', context)

def about(request):
    return render(request, 'bytenews/about.html', {'title': "About"})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            NewsletterSubscription.objects.create(email=email)
            return redirect('home')
    return render(request, 'news/subscribe.html')

def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'bytenews/post_form.html', {'form': form})

def post_delete_view(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'bytenews/post_list.html', {'posts': posts})