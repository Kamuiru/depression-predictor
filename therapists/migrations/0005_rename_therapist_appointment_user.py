# Generated by Django 4.2.1 on 2023-05-17 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('therapists', '0004_rename_appointmentbooked_appointment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='therapist',
            new_name='user',
        ),
    ]
