# Generated by Django 4.0.6 on 2022-07-18 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_calendario_categoria_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='imagem_evento',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]
