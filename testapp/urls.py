from django.urls import path
from .views import *

urlpatterns = [
    path("hello", hello_world, name="hello"),
    path("add_user", create_user, name="create user"),
    path("get_user", get_user, name="get user"),
    path("add_todo", add_todo, name="add todo"),
    path("get_todo", get_todo, name="get todo")
]