# Generated by Django 4.0.3 on 2022-03-05 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prayerboard', '0010_prayer_prayer_title_prayer_prayer_updates_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrayerUpdates',
        ),
    ]
