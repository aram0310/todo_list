from django.shortcuts import render, redirect
from . models import Todo
from .forms import TodoForm

# Create your views here.

def tasks(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request, 'todo_app/task_list.html', context= context)


def create(request):
    context = {}
    
    form = TodoForm(request.POST or None)
    if form.is_valid():
        print(form)
        form.save()
        return redirect(tasks)
        
    
    context['form'] = form
    
    return render(request, 'todo_app/create.html', context=context)


def todo_details(request, pk) :
    todo = Todo.objects.get(pk = pk)
    context = {
        'todo': todo,
    }
    
    return render(request, 'todo_app/todo_detail.html', context)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    print(todo)
    
    context = {
        'todo': todo
    }
    
    if request.POST:
        print('deleting')
        todo.delete()
        return redirect(tasks)
   
        
    return render(request, 'todo_app/confirm_deletion.html', context)
        
