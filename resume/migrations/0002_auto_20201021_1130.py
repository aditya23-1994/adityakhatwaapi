# Generated by Django 3.1.2 on 2020-10-21 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
