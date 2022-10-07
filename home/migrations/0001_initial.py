# Generated by Django 4.0.1 on 2022-03-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('password', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
