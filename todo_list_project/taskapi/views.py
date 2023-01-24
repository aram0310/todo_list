from django.shortcuts import render
from  django.http import JsonResponse, HttpResponse
from todo_app.models import Todo
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .serializers import TodoSerializer

# Create your views here.
@csrf_exempt
def tasks(request):
    
    # print(request.user)
    
    if request.method == 'GET':
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        
        return JsonResponse(todo_serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        
        
        serializer = TodoSerializer(data=data)
        

        if serializer.is_valid():
        
            serializer.save()
            return JsonResponse(serializer.data, status=201)

            # print(serializer.title)
            
        return JsonResponse(serializer.errors, status=400)
    
        
    
@csrf_exempt  
def task(request, pk):
    # retrive, update or delete a code 
    try:
        todo = Todo.objects.get(pk=pk) 
        
        if request.method == 'GET':
            print(todo)
            serializer = TodoSerializer(todo)
            return JsonResponse(serializer.data, safe=False)
        
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = TodoSerializer(todo, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
        
        elif request.method == "DELETE":
            todo.delete()
            return HttpResponse(status=204)
            

    except:
        print(pk)
        return HttpResponse({"msg": f"Todo with {id} not found"}, status=404)
    
    
    
    
    return JsonResponse({"msg": "None"})