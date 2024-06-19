from django.urls import path
from . import views 
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bytenews'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),

    #User Authentication 
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('login/', user_views.login, name="login"),
    path('logout/', user_views.logout, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)