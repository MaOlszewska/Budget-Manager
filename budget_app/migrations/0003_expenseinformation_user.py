# Generated by Django 4.0.2 on 2022-02-15 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget_app', '0002_alter_expenseinformation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseinformation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
