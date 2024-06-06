# Generated by Django 5.0.6 on 2024-06-06 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0005_tipoquestionario_tipodoquestionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='quemrespondeu',
            name='vinculo',
            field=models.IntegerField(blank=True, choices=[(0, 'Concursado'), (1, 'Contratado')], default=0, null=True, verbose_name='Vinculo'),
        ),
    ]
