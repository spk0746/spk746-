# Generated by Django 5.0.7 on 2024-07-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newapp', '0003_alter_user_email_alter_user_mobile_alter_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Age',
            field=models.IntegerField(default=0),
        ),
    ]
