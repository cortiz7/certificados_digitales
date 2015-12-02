# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20151201_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='guid',
            field=models.CharField(default=uuid.uuid4, unique=True, max_length=255),
        ),
    ]
