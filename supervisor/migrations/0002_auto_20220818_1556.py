# Generated by Django 3.1.6 on 2022-08-18 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supervisor',
            old_name='bank_acc_name',
            new_name='bank_acc_type',
        ),
    ]
