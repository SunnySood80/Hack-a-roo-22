# Generated by Django 4.0.3 on 2022-04-05 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0002_unregisteredusers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unregisteredusers',
            old_name='flag',
            new_name='issuedTicket',
        ),
    ]
