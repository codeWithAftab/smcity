# Generated by Django 3.2.4 on 2021-06-26 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='agent',
            fields=[
                ('agent_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_provider', models.CharField(max_length=30, null=True)),
                ('balance_amount', models.FloatField(default=0)),
                ('bank_acc_no', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=30)),
                ('bank_acc_name', models.CharField(max_length=50)),
                ('bank_ifsc', models.CharField(max_length=20)),
                ('agent_is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
