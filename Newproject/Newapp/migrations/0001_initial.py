# Generated by Django 5.0.7 on 2024-07-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Age', models.ImageField(max_length=3, null=True, upload_to='')),
                ('Address', models.CharField(max_length=100, null=True)),
                ('Mobile', models.IntegerField(max_length=16)),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
    ]
