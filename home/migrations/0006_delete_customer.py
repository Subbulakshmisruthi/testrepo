# Generated by Django 4.0.1 on 2022-03-23 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_customer_password1_alter_customer_password2_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customer',
        ),
    ]
