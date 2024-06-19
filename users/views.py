from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            print("User saved")
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username} Login Now')
            return redirect('bytenews:login')
        else:
            print("Form is not valid")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login_user(request, user)
                return render(request, 'bytenews/home.html')
        else:
            # Return an error message
            return render(request, 'users/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    

#the logout function
def logout(request):
    auth_logout(request)
    return redirect('bytenews:home')


#the profile function
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html', {'user': request.user})
    else:
        return redirect('bytenews:login')