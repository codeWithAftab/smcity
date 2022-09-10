# Generated by Django 4.1 on 2022-09-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0006_rename_agent_id_sup_agent_agent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sup_agent',
            name='status',
            field=models.CharField(choices=[(0, 'rejected'), (1, 'approved'), (2, 'pending')], default=2, max_length=30),
        ),
    ]
