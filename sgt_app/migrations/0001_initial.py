# Generated by Django 4.2.2 on 2023-06-23 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('fecha_vencimiento', models.DateField()),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
    ]
