# Generated by Django 4.1 on 2022-09-06 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0003_auto_20220803_1506'),
        ('supervisor', '0003_alter_sup_agent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sup_agent',
            name='sup_agent_id',
        ),
        migrations.AddField(
            model_name='sup_agent',
            name='agent_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='agent.agent'),
            preserve_default=False,
        ),
    ]
