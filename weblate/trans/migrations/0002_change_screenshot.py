# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 3.1.7 on 2021-03-19 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("screenshots", "0001_squashed_weblate_5"),
        ("trans", "0001_squashed_weblate_5"),
    ]
    replaces = [
        ("trans", "0129_auto_20210319_1419"),
    ]

    operations = [
        migrations.AddField(
            model_name="change",
            name="screenshot",
            field=models.ForeignKey(
                db_index=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="screenshots.screenshot",
            ),
        ),
    ]
