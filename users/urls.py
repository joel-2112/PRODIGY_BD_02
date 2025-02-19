from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.list_users, name='list_users'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/<str:pk>/', views.get_user, name='user_detail'),
    path('users/<str:pk>/update/', views.update_user, name='update_user'),
    path('users/<str:pk>/delete/', views.delete_user, name='delete_user'),
]
