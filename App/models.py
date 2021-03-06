from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
def is_esprit_mail(mail):
    if(str(mail).endswith("@esprit.tn")==False):
        raise ValidationError("email doit contenir @esprit.tn", params={'mail':mail})
class User(models.Model):
    nom=models.CharField(max_length=150)
    prenom=models.CharField(max_length=150)
    email=models.EmailField('Email',validators=[is_esprit_mail])
    def __str__(self):
        return f'le nom est {self.nom} le prenom est {self.prenom}'
class Etudiant(User):
    groupe=models.CharField(max_length=30)
class Coach(User):
    pass
class Project(models.Model):
    nom_projet=models.CharField('Titre du Projet',max_length=30)
    duree_projet=models.IntegerField(default=0)
    temps_alloue_par_createur=models.IntegerField('Temps Alloue',validators=[MinValueValidator(1), MaxValueValidator(10)])
    besoins=models.TextField(max_length=100)
    description=models.TextField(max_length=100)
    est_valide=models.BooleanField(default=False)
    createur=models.OneToOneField(
        Etudiant,
        on_delete=models.CASCADE,
        related_name='project_owner'
    )
    superviseur=models.ForeignKey(
        Coach,
        on_delete=models.SET_NULL,
        null=True,
        related_name='project_coach'
    )
    members=models.ManyToManyField(
        Etudiant,
        through='MemberShipInProject',
        related_name='Les_membres'
    )
class MemberShipInProject(models.Model):
    projet=models.ForeignKey(Project,on_delete=models.CASCADE)
    etudiant=models.ForeignKey(Etudiant,on_delete=models.CASCADE)
    Time_allocated_by_memebers=models.IntegerField()