# Generated by Django 4.2.1 on 2023-05-17 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_alter_feature_fs_meat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='children',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='cons_allfood',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='cons_ed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='cons_med_total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='edu',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='fs_meat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='hh_children',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='hhsize',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='feature',
            name='med_expenses_hh_ep',
            field=models.IntegerField(),
        ),
    ]
