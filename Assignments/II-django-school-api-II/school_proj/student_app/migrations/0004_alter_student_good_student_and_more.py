# Generated by Django 4.2.7 on 2023-11-20 23:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_alter_student_locker_combination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='good_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', max_length=8, validators=[django.core.validators.RegexValidator('^\\d{2}-\\d{2}-\\d{2}$', 'Invalid locker combination. Use the format "xx-xx-xx."')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_number',
            field=models.IntegerField(default=110, unique=True),
        ),
    ]
