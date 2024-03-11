# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.5 on 2023-09-18 08:30

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("metrics", "0001_initial"),
        ("metrics", "0002_import_user_metrics"),
        ("metrics", "0003_fixup_non_unique"),
        ("metrics", "0004_auto_20210330_0633"),
        ("metrics", "0005_add_missing_user"),
        ("metrics", "0006_auto_20210331_1047"),
        ("metrics", "0007_auto_20210402_1205"),
        ("metrics", "0008_alter_metric_value"),
        ("metrics", "0009_alter_metric_name"),
        ("metrics", "0010_alter_metric_options"),
        ("metrics", "0011_metric_kind"),
        ("metrics", "0012_migrate_kind"),
        ("metrics", "0013_auto_20210930_1841"),
        ("metrics", "0014_metricfuture"),
        ("metrics", "0015_migrate_metrics"),
        ("metrics", "0016_delete_metric"),
        ("metrics", "0017_rename_metricfuture_metric"),
        ("metrics", "0018_alter_metric_unique_together"),
    ]

    initial = True

    dependencies = [
        ("trans", "0001_squashed_weblate_5"),
        ("accounts", "0001_squashed_weblate_5"),
        ("weblate_auth", "0002_squashed_weblate_5"),
    ]

    operations = [
        migrations.CreateModel(
            name="Metric",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("date", models.DateField(default=datetime.date.today)),
                ("scope", models.SmallIntegerField()),
                ("relation", models.IntegerField()),
                ("secondary", models.IntegerField(default=0)),
                ("changes", models.IntegerField()),
                ("data", models.JSONField(null=True)),
            ],
            options={
                "verbose_name": "Metric",
                "verbose_name_plural": "Metrics",
                "unique_together": {("scope", "relation", "secondary", "date")},
            },
        ),
    ]