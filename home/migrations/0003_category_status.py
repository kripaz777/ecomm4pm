# Generated by Django 3.2.7 on 2021-09-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210914_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'inactive')], max_length=50),
        ),
    ]
