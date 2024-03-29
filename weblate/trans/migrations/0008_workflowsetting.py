# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.6 on 2023-10-13 06:25

import django.db.models.deletion
from django.db import migrations, models

import weblate.trans.validators


class Migration(migrations.Migration):
    dependencies = [
        ("lang", "0001_squashed_weblate_5"),
        ("trans", "0007_alter_change_action"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkflowSetting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "translation_review",
                    models.BooleanField(
                        default=False,
                        help_text="Requires dedicated reviewers to approve translations.",
                        verbose_name="Enable reviews",
                    ),
                ),
                (
                    "enable_suggestions",
                    models.BooleanField(
                        default=True,
                        help_text="Whether to allow translation suggestions at all.",
                        verbose_name="Turn on suggestions",
                    ),
                ),
                (
                    "suggestion_voting",
                    models.BooleanField(
                        default=False,
                        help_text="Users can only vote for suggestions and can’t make direct translations.",
                        verbose_name="Suggestion voting",
                    ),
                ),
                (
                    "suggestion_autoaccept",
                    models.PositiveSmallIntegerField(
                        default=0,
                        help_text="Automatically accept suggestions with this number of votes, use 0 to turn it off.",
                        validators=[weblate.trans.validators.validate_autoaccept],
                        verbose_name="Autoaccept suggestions",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="lang.language"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.project",
                    ),
                ),
            ],
        ),
    ]
