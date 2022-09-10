from django.urls import path 
from base.views import  TaskList
from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('task-list', TaskList.as_view(), name='task-list'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<int:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<int:pk>/', views.delete_task, name='task-delet'),
]
