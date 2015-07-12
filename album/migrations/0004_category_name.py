# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_remove_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=datetime.date(2015, 7, 11), max_length=50),
            preserve_default=False,
        ),
    ]
