# Generated by Django 3.0.6 on 2020-06-03 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messages',
            new_name='message',
        ),
    ]
