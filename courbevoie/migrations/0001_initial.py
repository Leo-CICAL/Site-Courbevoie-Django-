# Generated by Django 3.0.6 on 2020-05-12 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foyer',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('mdp', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('num_tel', models.CharField(max_length=10)),
                ('adresse', models.CharField(max_length=200)),
                ('nombre_enfants', models.IntegerField()),
                ('enceinte', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Magasin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('nb_commande', models.IntegerField(default=0)),
                ('magasin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courbevoie.Magasin')),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=200)),
                ('restriction', models.CharField(max_length=200)),
                ('foyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courbevoie.Foyer')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date de la Commande')),
                ('foyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courbevoie.Foyer')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courbevoie.Produit')),
            ],
        ),
    ]
