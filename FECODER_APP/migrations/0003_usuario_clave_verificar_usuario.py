# Generated by Django 4.0.5 on 2022-07-10 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FECODER_APP', '0002_comentario_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='clave_verificar_usuario',
            field=models.CharField(default='', max_length=8),
        ),
    ]
