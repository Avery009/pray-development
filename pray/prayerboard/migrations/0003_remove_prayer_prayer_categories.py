# Generated by Django 3.2.4 on 2022-01-22 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prayerboard', '0002_alter_prayer_prayer_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prayer',
            name='prayer_categories',
        ),
    ]
