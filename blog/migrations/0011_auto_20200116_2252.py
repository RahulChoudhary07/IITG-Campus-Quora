# Generated by Django 2.2 on 2020-01-16 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_notifications'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notifications',
            options={'ordering': ['-created_on']},
        ),
    ]
