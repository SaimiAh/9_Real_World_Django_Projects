from django.urls import path
from . import views
urlpatterns = [
    path('Resume/', views.about, name="Resume"),

]