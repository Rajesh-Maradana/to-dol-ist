from django.urls import path
from . import views

urlpatterns = [
path('',views.home), 
path('todo/',views.todo),
path('delete/<int:todo_id>',views.delete),

]