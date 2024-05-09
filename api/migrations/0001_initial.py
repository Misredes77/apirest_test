# Generated by Django 5.0.4 on 2024-04-18 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=128)),
                ('salario_base', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
