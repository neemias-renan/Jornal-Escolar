# Generated by Django 4.1.6 on 2023-02-09 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inrite', '0004_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
