# Generated by Django 2.2.13 on 2021-01-25 15:48

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_category_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='uniq', editable=False, populate_from='name', unique=True, verbose_name='Category Link'),
            preserve_default=False,
        ),
    ]
