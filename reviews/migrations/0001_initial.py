# Generated by Django 4.2.3 on 2023-08-02 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('onlines', '0001_initial'),
        ('offlines', '0001_initial'),
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('textArea', models.TextField()),
                ('rating', models.PositiveIntegerField()),
                ('challenge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='challenges.challenge')),
                ('offline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='offlines.offline')),
                ('online', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='onlines.online')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
