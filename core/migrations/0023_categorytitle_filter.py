# Generated by Django 4.2.2 on 2023-10-27 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_categorytitle_alter_portfolio_media_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytitle',
            name='filter',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]