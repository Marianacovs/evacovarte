# Generated by Django 5.0.7 on 2024-09-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0006_alter_contacto_avisos_alter_contacto_correo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
