# Generated by Django 4.0.4 on 2022-08-20 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('entry_no', models.CharField(max_length=30)),
                ('programme', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('valid_upto', models.DateField()),
                ('emergency_no', models.CharField(default='', max_length=20)),
                ('blood_group', models.CharField(default='', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
