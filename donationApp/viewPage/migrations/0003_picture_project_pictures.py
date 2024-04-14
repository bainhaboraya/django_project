# Generated by Django 5.0.4 on 2024-04-14 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewPage', '0002_remove_project_created_at_remove_project_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to='images')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_pictures', to='viewPage.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='pictures',
            field=models.ManyToManyField(blank=True, related_name='projects', to='viewPage.picture'),
        ),
    ]