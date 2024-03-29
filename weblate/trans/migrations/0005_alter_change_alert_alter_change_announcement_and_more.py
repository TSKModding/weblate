# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.5 on 2023-10-11 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("screenshots", "0001_squashed_weblate_5"),
        ("trans", "0004_alter_change_action"),
    ]

    operations = [
        migrations.AlterField(
            model_name="change",
            name="alert",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="trans.alert",
            ),
        ),
        migrations.AlterField(
            model_name="change",
            name="announcement",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="trans.announcement",
            ),
        ),
        migrations.AlterField(
            model_name="change",
            name="comment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="trans.comment",
            ),
        ),
        migrations.AlterField(
            model_name="change",
            name="screenshot",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="screenshots.screenshot",
            ),
        ),
        migrations.AlterField(
            model_name="change",
            name="suggestion",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="trans.suggestion",
            ),
        ),
    ]
