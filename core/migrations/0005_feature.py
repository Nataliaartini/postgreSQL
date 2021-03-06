# Generated by Django 4.0.4 on 2022-05-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_team_member_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('feature_name', models.CharField(max_length=100, verbose_name='Recurso')),
                ('feature_description', models.TextField(blank=True, verbose_name='Descrição')),
                ('feature_icon', models.CharField(max_length=12, verbose_name='Ícone')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
