# Generated by Django 4.0.4 on 2024-05-20 14:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_sectiononequestions_average_hours_per_day_at_work_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=15, null=True, region=None),
        ),
    ]
