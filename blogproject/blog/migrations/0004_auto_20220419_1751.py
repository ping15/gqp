# Generated by Django 2.2.3 on 2022-04-19 09:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220417_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 9, 51, 51, 779390, tzinfo=utc), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 9, 51, 51, 778204, tzinfo=utc), verbose_name='创建时间'),
        ),
    ]
