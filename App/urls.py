from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import Affiche_ListView, CreateProject, DeleteGeneric
from . import views

urlpatterns=[
    path('index/', views.index),
    path('index_c/<int:classe>/',views.index_id),
    path('t/',views.template),
    path('Affiche/', views.Affiche),
    path('Affiche_ListView/', Affiche_ListView.as_view(), name="LV"),
    path('Ajout/',views.add_project, name="ajout"),
    path('CreateP/',CreateProject.as_view()),
    path('Delete/<int:id>',views.Delete,name='D'),
    path('DeleteP/<int:pk>', DeleteGeneric.as_view(), name="DD"),
    path('Acceuil/',views.Acceuil, name="accueil"),
    path('Login/', views.login_user,name='login'),
    path('register/',views.register,name='re'),
    path('Logout/',views.Deconnecter, name='logout'),
    path('login2/',LoginView.as_view(template_name='App/login.html'),name='login2'),
    path('logout2/',LogoutView.as_view(),name='logout2')



]