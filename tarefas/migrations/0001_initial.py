# Generated by Django 3.2.10 on 2021-12-19 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=300)),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
