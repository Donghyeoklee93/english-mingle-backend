# Generated by Django 4.0.10 on 2023-07-31 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('onlines', '0001_initial'),
        ('medias', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='online',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='onlines.online'),
        ),
    ]
