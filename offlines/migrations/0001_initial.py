# Generated by Django 4.0.10 on 2023-07-31 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        ('levels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="student's name only", max_length=150, verbose_name='student name')),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=150)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='levels.level')),
                ('subjects', models.ManyToManyField(to='subjects.subject')),
            ],
            options={
                'verbose_name_plural': 'offline_classes',
            },
        ),
    ]
