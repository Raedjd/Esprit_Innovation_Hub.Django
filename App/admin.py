from django.contrib import admin, messages

# Register your models here.
from .models import *
class members(admin.TabularInline):
    model = MemberShipInProject
    extra=1
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def set_to_valid(self,request,queryset):
        queryset.update(est_valide=True)
    actions = ['set_to_valid','set_to_no_valid']
    set_to_valid.short_description="Valider"
    def set_to_no_valid(self,request,queryset):
        rows=queryset.filter(est_valide=False)
        a=rows.count()
        if a>0:
            messages.error(request, "%s projets valide" % a)
        else:
            rows_updated=queryset.update(est_valide=False)
            if rows_updated==1:
                message="1 project was updates"
            else:
                message="%s projects were updates" % rows_updated
            self.message_user(request,message)


    set_to_no_valid.short_description="Refuser"
    list_display = ('nom_projet','duree_projet',
                    'temps_alloue_par_createur',
                    'description','besoins','est_valide')
    list_per_page = 2
    inlines = (members,)
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ('est_valide','createur__prenom')
    #Barre de recherche
    search_fields = ['nom_projet','duree_projet']
admin.site.register(Etudiant)
admin.site.register(Coach)
#admin.site.register(Project,ProjectAdmin)