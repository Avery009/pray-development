# Generated by Django 3.2.4 on 2022-02-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayerboard', '0008_auto_20220205_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prayer',
            name='prayer_count',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
