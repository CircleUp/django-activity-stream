# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='visibility',
            field=models.IntegerField(default=1, choices=[(0, 'All'), (1, 'Limited'), (2, 'Public only')]),
            preserve_default=True,
        ),
    ]
