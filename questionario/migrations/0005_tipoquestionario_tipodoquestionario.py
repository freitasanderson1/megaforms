# Generated by Django 5.0.6 on 2024-06-05 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0004_alter_itemassociativo_opcao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoquestionario',
            name='tipoDoQuestionario',
            field=models.IntegerField(blank=True, choices=[(0, 'Pré-Teste'), (1, 'Pós-Teste')], default=0, null=True, verbose_name='Tipos de questionário'),
        ),
    ]
