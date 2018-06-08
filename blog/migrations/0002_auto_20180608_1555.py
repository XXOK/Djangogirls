# Generated by Django 2.0.4 on 2018-06-08 06:55

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default=blog.models.get_random_name, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, help_text='최대 300자 내외', max_length=300, verbose_name='내용'),
        ),
    ]
