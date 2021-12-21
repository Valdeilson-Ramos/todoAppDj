from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa
# Create your views here.
def index(request):
    tarefa=Tarefa.objects.all()
    context={
        'tarefa':tarefa,
    }
    return render(request, 'tarefa/index.html', context)
 