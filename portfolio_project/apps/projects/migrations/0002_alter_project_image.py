# Generated by Django 3.2.3 on 2021-05-30 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='portfolio_project/apps/projects/static/media/'),
        ),
    ]