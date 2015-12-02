# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='guid',
            field=models.CharField(default=uuid.uuid4, unique=True, max_length=13),
        ),
    ]
