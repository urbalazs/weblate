# -*- coding: utf-8 -*-
# Generated by Django 2.2.5 on 2019-12-12 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("trans", "0054_auto_20191212_1441")]

    operations = [
        migrations.RenameField(model_name="unit", old_name="comment", new_name="note"),
        migrations.RemoveField(model_name="suggestion", name="language"),
        migrations.AlterField(
            model_name="comment",
            name="unit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="trans.Unit"
            ),
        ),
    ]
