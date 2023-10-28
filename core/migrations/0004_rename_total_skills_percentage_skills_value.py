# Generated by Django 4.2.2 on 2023-10-22 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_skills_alter_testimonials_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='total',
            new_name='percentage',
        ),
        migrations.AddField(
            model_name='skills',
            name='value',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]