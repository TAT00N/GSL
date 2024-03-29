# Generated by Django 5.0.2 on 2024-02-28 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsl_cargo', '0001_initial'),
        ('gsl_clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gslpapeleriacargo',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsl_clientes.gslclientes'),
        ),
        migrations.AlterField(
            model_name='gslgastoscargo',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsl_clientes.gslclientes'),
        ),
        migrations.AlterField(
            model_name='gslcargo',
            name='nombre_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsl_clientes.gslclientes'),
        ),
        migrations.DeleteModel(
            name='GSLClientes',
        ),
    ]
