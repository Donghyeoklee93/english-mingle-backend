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
            name='Online',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='class name only', max_length=150, verbose_name='class name')),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('kind', models.CharField(choices=[('20MINS', '20MINS'), ('40MINS', '40MINS'), ('60MINS', '60MINS')], max_length=20)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='levels.level')),
                ('subjects', models.ManyToManyField(related_name='classes', to='subjects.subject')),
            ],
            options={
                'verbose_name_plural': 'online_classes',
            },
        ),
    ]
