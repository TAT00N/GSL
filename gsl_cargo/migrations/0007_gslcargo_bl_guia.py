# Generated by Django 5.0.2 on 2024-03-01 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsl_cargo', '0006_alter_gslcargo_fecha_arribo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gslcargo',
            name='bl_guia',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
