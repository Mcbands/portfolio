# Generated by Django 4.2.2 on 2023-10-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_about_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Degree',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
