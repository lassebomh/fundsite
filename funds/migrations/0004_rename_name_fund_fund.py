# Generated by Django 4.1.7 on 2023-03-07 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0003_rename_first_name_investor_investor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fund',
            old_name='name',
            new_name='fund',
        ),
    ]
