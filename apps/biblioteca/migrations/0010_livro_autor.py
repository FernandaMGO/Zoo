# Generated by Django 4.2 on 2023-04-16 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0009_rename_biblioteca_livro'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.CharField(default=None, max_length=100),
        ),
    ]