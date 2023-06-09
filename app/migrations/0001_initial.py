# Generated by Django 4.1 on 2023-05-31 15:30

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to='files', validators=[app.models.validate_file_size])),
            ],
        ),
    ]
