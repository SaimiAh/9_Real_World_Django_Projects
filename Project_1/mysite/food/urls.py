from . import views
from django.urls import path
app_name = 'food'
urlpatterns = [
    #/food/ home url
    path('', views.index, name='index'),
    #/food/1 item detail url
    path('<int:item_id>/', views.details, name='details'),
    #item
    path('item/', views.item, name='item'),
    #/food/add additem 
    path('add/', views.create_item, name='create_item'),
    #/food/update/1 upadate a specific item
    path('update/<int:id>/', views.update_item, name='update_item'),
    #/ delete a specific item
    path('delete/<int:id>/', views.delete_item, name='deletes_item'),
]