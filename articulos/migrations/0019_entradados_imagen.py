# Generated by Django 5.0.7 on 2024-09-23 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0018_entradados_alter_entradas_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradados',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
