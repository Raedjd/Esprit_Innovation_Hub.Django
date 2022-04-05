from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .forms import AddProjectForm
from .models import Project


def index(request):
    return HttpResponse("bonjour 4TWIN6")
def index_id(request, classe):
    return HttpResponse(' Bonjour %s' % classe)
def template(request):
    return render(request,'App/Affiche.html')
@login_required(login_url='login')
def Affiche(request):
    projet=Project.objects.all()#==>select *
    #resultat='-'.join([p.nom_projet for p in projet ])
    #return HttpResponse(resultat)
    return render(request,'App/Affiche.html',
                  {'pp':projet})

class Affiche_ListView(LoginRequiredMixin,ListView):
    model= Project
    template_name = 'App/Affiche.html'
    context_object_name = 'pp'
    #ordering=['-description']
    #fields="__all__"
def add_project(request):
    if request.method=="GET":
        form=AddProjectForm()
        return render(request,'App/ajout.html',
                      {'f':form})
    if request.method=="POST":
        form = AddProjectForm(request.POST)
        if form.is_valid():
            new_project=form.save(commit=False)
            new_project.save()
            return HttpResponseRedirect(reverse('LV'))
        else:
            return render(request,'App/ajout.html',
                      {'f':form,'msg_erreur':"Erreur lors de l'ajout d'un projet"})
class CreateProject(CreateView):
    model = Project
    fields = ['nom_projet',
                'duree_projet','temps_alloue_par_createur',
                'besoins','description',
                'est_valide','createur']
    success_url = reverse_lazy('LV')
def Delete(request, id):
    projet=Project.objects.get(pk=id)
    #projet=get_object_or_404(Project,pk=id)
    projet.delete()
    return HttpResponseRedirect(reverse('LV'))

class DeleteGeneric(DeleteView):
    model = Project
    success_url = reverse_lazy('LV')

def Acceuil(request):
    return render(request,'base.html')
def login_user(request):
    if request.method =="POST":
        u=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=u,password=password)
        if user is not None:
            login(request,user)
            return redirect('accueil')
        else:
            messages.info(request,'Username or Password incorrect')
            return redirect('login')

    else:
        return render(request,'App/login.html')

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'App/signup.html',{'f':form})


def Deconnecter(request):
    logout(request)
    return redirect('login')