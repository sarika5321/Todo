from django.shortcuts import render
from app.models import *
from django.http import HttpResponse 
# Create your views here.

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        TO = Todo(title=title, desc=desc)
        TO.save()
    alltodos = Todo.objects.all()
    d = {'alltodos':alltodos}
    return render(request, 'index.html', d)