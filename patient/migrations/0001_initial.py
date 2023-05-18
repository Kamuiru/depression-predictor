# Generated by Django 4.2.1 on 2023-05-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('femaleres', models.BooleanField(default=True)),
                ('age', models.FloatField()),
                ('married', models.BooleanField(default=True)),
                ('children', models.FloatField()),
                ('hhsize', models.FloatField()),
                ('edu', models.FloatField()),
                ('hh_children', models.FloatField()),
                ('cons_allfood', models.FloatField()),
                ('cons_med_total', models.FloatField()),
                ('cons_ed', models.FloatField()),
                ('ent_wagelabor', models.BooleanField()),
                ('ent_ownfarm', models.BooleanField()),
                ('ent_business', models.BooleanField()),
                ('ent_nonagbusiness', models.BooleanField()),
                ('fs_meat', models.IntegerField()),
                ('fs_enoughtom', models.BooleanField()),
                ('fs_sleephun', models.BooleanField()),
                ('med_expenses_hh_ep', models.FloatField()),
                ('labor_primary', models.BooleanField()),
            ],
        ),
    ]