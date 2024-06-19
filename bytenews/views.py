from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, NewsletterSubscription
from .models import Post

# Define a list of posts


# Define a function to handle the home page
def home(request):
    featured_post = Post.objects.filter(featured=True).first()
    print(featured_post)

    trending_post = Post.objects.filter(trending=True).first()
    print(trending_post)

    context = {
        'posts': Post.objects.all(),
        'featured_post': featured_post,
        'trending_post': trending_post
    }
    return render(request, 'bytenews/home.html', context)

# function to handle the about page
def about(request):
    return render(request, 'bytenews/about.html', {'title': "About"})

#  function to handle newsletter subscriptions
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            NewsletterSubscription.objects.create(email=email)
            return redirect('home')
    return render(request, 'news/subscribe.html')



def post_list_view(request):
    featured_post = Post.objects.filter(featured=True).first()
    return render(request, 'home.html', {'posts': [featured_post]})

