from django.urls import path
from .views import index, addTodoView, deleteTodoView

urlpatterns = [
    path('', index, name='home'),
    path('addTodoItems/', addTodoView, name='add-todo'),
    path('deleteTodoItem/<int:i>/', deleteTodoView, name='delete-todo'), 
]