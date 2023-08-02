# Generated by Django 4.2.3 on 2023-08-02 20:05

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
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='class name only', max_length=150, verbose_name='class name')),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('kind', models.CharField(choices=[('LVEC', 'LVEC'), ('UEEC', 'UEEC'), ('EDEC', 'EDEC')], max_length=20)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='levels.level')),
                ('subjects', models.ManyToManyField(to='subjects.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
