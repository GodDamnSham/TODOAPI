import json
from django.http import HttpResponse
from rest_framework import generics , status
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import taskSerializer
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
#show Tasklist
class TaskList(generics.ListCreateAPIView ):
    serializer_class = taskSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user.id)
        return queryset
    
''' @api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = taskSerializer(tasks, many = True)
    return Response(serializer.data) '''

#create task
@api_view(['POST'])
def taskCreate(request):
    permission_classes = [IsAuthenticated]

    serializer = taskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)

@api_view(["POST"])
def taskUpdate(request, pk):
    permission_classes = [IsAuthenticated]
    task = Task.objects.get(pk = pk)
    serializer = taskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@csrf_exempt
def delete_task(request, pk , format=None):
    permission_classes = [IsAuthenticated]
    task = Task.objects.get(pk=pk)
    task.delete()
    #return redirect('task-list')
    return HttpResponse(status=204)


