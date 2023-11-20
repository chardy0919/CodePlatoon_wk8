# Generated by Django 4.2.7 on 2023-11-20 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('student_email', models.EmailField(max_length=254)),
                ('personal_email', models.EmailField(max_length=254)),
                ('locker_number', models.IntegerField()),
                ('locker_combination', models.CharField()),
                ('good_student', models.BooleanField()),
            ],
        ),
    ]
