# Generated by Django 4.1.5 on 2023-01-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='recruiter_notes',
            field=models.TextField(blank=True),
        ),
    ]
