from django.urls import path
from . import views
urlpatterns = [
    path('Images/', views.gallery, name="Gallery")
]