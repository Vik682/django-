# Generated by Django 4.0.4 on 2022-05-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_student_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
