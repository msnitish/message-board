from django.urls import path, include
from .views import message_list, create_message, delete_message

urlpatterns = [
    # path('api/', include('messages.urls')),
    path('messages', message_list, name='message-list'),
    path('create-message', create_message, name='create-message'),
    path('delete-message/<int:id>/', delete_message, name='delete-message'),
]
