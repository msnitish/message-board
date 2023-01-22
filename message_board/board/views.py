from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer

# Create your views here.


@api_view(['GET'])
def message_list(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect('message-list')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_message(request, id):
    message = Message.objects.filter(id=id).first()
    if message:
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND)