# Generated by Django 4.2.3 on 2023-07-17 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_department_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='Role',
        ),
    ]
