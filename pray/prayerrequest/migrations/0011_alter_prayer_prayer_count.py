# Generated by Django 3.2.4 on 2022-02-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayerrequest', '0010_alter_prayer_prayer_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='prayer_count',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
