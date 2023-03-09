# Generated by Django 3.2.6 on 2021-08-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colormodel',
            name='code',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='title',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]