from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import TodoListItem
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'home/index.html')
    else:
        all_todo_items = TodoListItem.objects.all().filter(user=request.user)
        return render(request, 'home/index.html', {"all_items": all_todo_items})

@login_required
def addTodoView(request):
    todo_list = request.POST['content']
    save_new_item = TodoListItem(user=request.user, content = todo_list)
    save_new_item.save()
    return redirect('home')

@login_required
def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id=i, user=request.user)
    y.delete()
    return redirect('home')