# Generated by Django 4.2.3 on 2023-07-29 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('onlines', '0001_initial'),
        ('bookings', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='online',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='onlines.online'),
        ),
    ]
