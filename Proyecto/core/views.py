from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores":consulta}
    return render(request, "core/profesor_list.html", contexto)

def profesor_create(request):
    if request.method == "POST":
        form = forms.ProfesoForm(request.POST)
        if form.is_valid():
            form.save()
            return ("profesor_list")
    else:
        form = forms.ProfesoForm()
        return render(request, "core/profesor_create.html", {"form":form})