# Generated by Django 2.0.2 on 2018-03-13 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180313_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefprimeexcellence',
            name='annee',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='benefprimeexcellence',
            name='beneficiaires',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='benefprimeexcellence',
            name='code_academie',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='benefprimeexcellence',
            name='code_groupe_corps',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='benefprimeexcellence',
            name='code_region',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='benefprimeexcellence',
            name='code_secteur_cnu',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='benefprimeexcellence',
            name='code_sexe',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='benefprimeexcellence',
            name='secteur_disciplinaire',
            field=models.CharField(max_length=100, null=True),
        ),
    ]