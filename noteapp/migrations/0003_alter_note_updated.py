# Generated by Django 5.2 on 2025-04-26 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_alter_note_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
