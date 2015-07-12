# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='Category',
            new_name='category',
        ),
    ]
