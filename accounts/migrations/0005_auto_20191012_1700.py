# Generated by Django 2.2.3 on 2019-10-12 11:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20191012_1649'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UwerProfile',
            new_name='UserProfile',
        ),
    ]
