# Generated by Django 3.2.9 on 2023-03-18 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userroles',
            name='user_role',
            field=models.CharField(max_length=20),
        ),
    ]
