# Generated by Django 5.2.3 on 2025-06-28 15:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socialapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_perfil', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('matricula_perfil', models.CharField(max_length=255)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='perfil_fotos/')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_telefone', models.CharField(max_length=20)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefones', to='usuario.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_associacao', models.DateTimeField(auto_now_add=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.perfil')),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialapp.postagem')),
            ],
            options={
                'unique_together': {('perfil', 'postagem')},
            },
        ),
    ]
