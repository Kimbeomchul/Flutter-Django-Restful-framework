# Generated by Django 2.2.1 on 2019-11-24 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20191124_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='_id',
            new_name='nickname',
        ),
    ]