# Generated by Django 4.2.2 on 2023-10-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Total Count',
                'verbose_name_plural': 'Total Counts',
            },
        ),
    ]
