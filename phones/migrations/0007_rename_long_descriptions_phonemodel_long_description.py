# Generated by Django 3.2.6 on 2021-08-19 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_rename_long_description_phonemodel_long_descriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonemodel',
            old_name='long_descriptions',
            new_name='long_description',
        ),
    ]