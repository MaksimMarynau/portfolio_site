# Generated by Django 3.2.3 on 2021-06-13 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20210605_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, default='projects/additional/no-image.jpg', upload_to='projects/additional/')),
                ('project', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
