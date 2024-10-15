from urllib import request

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from ToDo_App.forms import TODoform
from ToDo_App.models import Task
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        Priority=request.POST.get('Priority','')
        Tdate=request.POST.get('Tdate','')
        task=Task(name=name,priority=Priority,Tdate=Tdate)
        task.save()

    return render(request,'index.html',{'task':task1})

# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskid):
    task = Task.objects.get(id=taskid)
    FT = TODoform(request.POST or None,instance=task)
    if FT.is_valid():
        FT.save()
        return redirect('/')
    return render(request, 'edit.html',{'Ft':FT,'Task':task})


class ListTask(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'

class ShowDetails(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','Tdate')
    def get_prefix(self):
        return  reverse_lazy('vDetails')

class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('vHome')