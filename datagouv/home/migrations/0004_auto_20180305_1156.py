# Generated by Django 2.0.2 on 2018-03-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180305_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effectifregional',
            name='donnees_soumises_au_secret_stat',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
