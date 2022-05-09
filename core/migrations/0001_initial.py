# Generated by Django 4.0.4 on 2022-05-09 20:33

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('product_name', models.CharField(max_length=100, verbose_name='Produto')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('icon', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Crescimento'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=12, verbose_name='Ícone')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('role_name', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('member_name', models.CharField(max_length=50, verbose_name='Nome')),
                ('member_bio', models.TextField(blank=True, max_length=200, verbose_name='Biografia')),
                ('member_photo', stdimage.models.StdImageField(upload_to='team', verbose_name='Foto')),
                ('member_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.role', verbose_name='Cargo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
