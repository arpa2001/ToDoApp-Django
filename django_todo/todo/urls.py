from django.urls import path
from . import views


urlpatterns = [
    path("", views.CreateTodoAPIView.index, name="index"),
    path("update/<int:pk>/", views.UpdateTodoAPIView.update_task, name="update_task"),
    path("delete/<int:pk>/", views.DeleteTodoAPIView.delete_task, name="delete_task"),
    path("api/", views.ListTodoAPIView.as_view(), name="todo_list"),
    path("api/create/", views.CreateTodoAPIView.as_view(), name="todo_create"),
    path("api/update/<int:pk>/",
         views.UpdateTodoAPIView.as_view(), name="update_todo"),
    path("api/delete/<int:pk>/",
         views.DeleteTodoAPIView.as_view(), name="delete_todo")
]
