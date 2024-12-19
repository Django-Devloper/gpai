# Generated by Django 5.1.3 on 2024-12-19 04:57

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectModelTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 19, 4, 57, 8, 557196, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 19, 4, 57, 8, 557196, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 19, 4, 57, 8, 557196, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('seed', models.PositiveIntegerField()),
                ('training_end', models.DateTimeField(blank=True, null=True)),
                ('duration', models.TimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SampleImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('object_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagetraining.objectmodeltraining')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('object_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imagetraining.objectmodeltraining')),
            ],
        ),
    ]
