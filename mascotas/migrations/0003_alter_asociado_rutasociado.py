# Generated by Django 4.1.4 on 2023-06-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_rename_asociados_asociado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociado',
            name='rutAsociado',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Rut del asociado'),
        ),
    ]