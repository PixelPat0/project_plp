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


    #post code
    path('post/create/', views.post_create_view, name='post_create'),
    path('post/delete/<pk>/', views.post_delete_view, name='post_delete'),
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/', views.post_list_view, name='post_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)