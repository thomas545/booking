# Generated by Django 3.0.8 on 2020-08-07 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0003_auto_20200803_2332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realty',
            old_name='title',
            new_name='name',
        ),
    ]
