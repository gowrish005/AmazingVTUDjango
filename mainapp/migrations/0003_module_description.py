# Generated by Django 5.1.1 on 2025-01-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_year_branch_semester_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
