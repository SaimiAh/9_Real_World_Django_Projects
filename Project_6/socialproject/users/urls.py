from django.urls import path
from re import template
from users import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', views.user_login, name='login'),
]