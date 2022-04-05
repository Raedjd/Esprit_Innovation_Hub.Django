# Generated by Django 3.2 on 2022-02-07 13:09

import App.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_projet', models.CharField(max_length=30, verbose_name='Titre du Projet')),
                ('duree_projet', models.IntegerField(default=0)),
                ('temps_alloue_par_createur', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Temps Alloue')),
                ('besoins', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('est_valide', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=150)),
                ('prenom', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, validators=[App.models.is_esprit_mail], verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='App.user')),
            ],
            bases=('App.user',),
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='App.user')),
                ('groupe', models.CharField(max_length=30)),
            ],
            bases=('App.user',),
        ),
        migrations.CreateModel(
            name='MemberShipInProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time_allocated_by_memebers', models.IntegerField()),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.project')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='createur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to='App.etudiant'),
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='Les_membres', through='App.MemberShipInProject', to='App.Etudiant'),
        ),
        migrations.AddField(
            model_name='project',
            name='superviseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_coach', to='App.coach'),
        ),
    ]
