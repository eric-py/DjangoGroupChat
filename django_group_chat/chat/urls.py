from django.urls import path, include

from . import views

app_name = 'chat'


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_chat, name='create_chat'),
    path('<str:chat_id>/', views.chat, name='chat'),
    path('<str:chat_id>/leave/', views.leave_chat, name='leave_chat'),
]