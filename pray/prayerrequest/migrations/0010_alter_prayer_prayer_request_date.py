# Generated by Django 3.2.4 on 2022-02-05 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayerrequest', '0009_auto_20220205_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='prayer_request_date',
            field=models.DateField(verbose_name='prayer request date'),
        ),
    ]
