# Generated by Django 4.2.4 on 2023-12-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=80)),
                ('user_email', models.CharField(max_length=200)),
                ('user_mobile', models.CharField(max_length=12)),
                ('user_created', models.DateTimeField()),
                ('password', models.CharField(max_length=400)),
            ],
        ),
    ]
