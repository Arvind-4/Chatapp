# Generated by Django 3.2.7 on 2021-10-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_contact_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='contact',
            name='company_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
