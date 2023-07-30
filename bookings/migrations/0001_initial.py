# Generated by Django 4.2.3 on 2023-07-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kind', models.CharField(choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE'), ('CHALLENGE', 'CHALLENGE')], max_length=15)),
                ('time_from', models.DateField(blank=True, null=True)),
                ('time_to', models.DateField(blank=True, null=True)),
                ('online_offline_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
