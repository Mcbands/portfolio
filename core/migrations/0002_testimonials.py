# Generated by Django 4.2.2 on 2023-10-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='OurTeam_images/')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name': 'OurTeam',
                'verbose_name_plural': 'OurTeams',
            },
        ),
    ]
