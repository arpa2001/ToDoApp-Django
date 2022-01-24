from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from todo.serializers import TodoSerializer
from todo.serializers2 import TodoSerializer2
from todo.models import Todo


class ListTodoAPIView(ListAPIView):
    """Lists all todos from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer2


class CreateTodoAPIView(CreateAPIView):
    """Creates a new todo"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer2

    def index(request):
        form = TodoSerializer()

        if request.method == "POST":
            form = TodoSerializer(request.POST)
            #return render(request, "testing.html", {"text": form})
            if form.is_valid():
                form.save()
                
            return redirect("index")

        tasks = Todo.objects.all()
        return render(request, "index.html", {"task_form": form, "tasks": tasks})



class UpdateTodoAPIView(UpdateAPIView):
    """Update the todo whose id has been passed through the request"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer2

    def update_task(request, pk):
        task = Todo.objects.get(id=pk)

        form = TodoSerializer(instance=task)

        if request.method == "POST":
            form = TodoSerializer(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("index")

        return render(request, "update_task.html", {"task_edit_form": form})



class DeleteTodoAPIView(DestroyAPIView):
    """Deletes a todo whose id has been passed through the request"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer2

    def delete_task(request, pk):
        task = Todo.objects.get(id=pk)
        task.delete()
        return redirect("index")
