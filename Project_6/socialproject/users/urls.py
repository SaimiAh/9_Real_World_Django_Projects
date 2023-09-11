from django.urls import path
from re import template
from users import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', views.user_login, name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'users/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeView.as_view(template_name = 'users/password_change_done.html'), name='password_change_done'),

]