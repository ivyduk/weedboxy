# Generated by Django 4.1.12 on 2023-10-30 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_useraccount_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='order',
        ),
    ]
