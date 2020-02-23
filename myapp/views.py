from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from myapp.models import Todo

def home(request):
   todo_items=Todo.objects.all().order_by('add_date')
   return render(request,'home.html',{"todo_items":todo_items})


@csrf_exempt

def todo(request):
   date=timezone.now()
   data=request.POST['list1']
   Todo.objects.create(add_date=date,text=data)
   return HttpResponseRedirect("/")

@csrf_exempt
def delete(request,todo_id):
   Todo.objects.get(id=todo_id).delete()
   return HttpResponseRedirect("/")

# Create your views here.