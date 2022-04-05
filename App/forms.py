from django import forms
from django.forms import Textarea

from .models import Project


class AddProjectForm(forms.ModelForm):
    class Meta:
        model= Project
        fields=('nom_projet',
                'duree_projet','temps_alloue_par_createur',
                'besoins','description',
                'est_valide','createur')
        widgets={'besoins':Textarea(
            attrs={'cols':20,'rows':20})}
