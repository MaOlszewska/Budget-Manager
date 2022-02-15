# Generated by Django 4.0.2 on 2022-02-15 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0003_expenseinformation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseinformation',
            name='category',
            field=models.CharField(choices=[('Zakupy', 'Zakupy'), ('Kosmetyki', 'Kosmetyki'), ('Odzież', 'Odzież'), ('Transport', 'Transport'), ('Rozrywka', 'Rozrywka'), ('Edukacja', 'Edukacja'), ('Inne', 'Inne')], default='Inne', max_length=10),
        ),
        migrations.AlterField(
            model_name='expenseinformation',
            name='expense',
            field=models.FloatField(),
        ),
    ]