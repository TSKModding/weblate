# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.5 on 2023-09-18 08:13

import django.core.files.storage
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import weblate.fonts.validators
import weblate.trans.mixins
from weblate.utils.data import data_dir


class Migration(migrations.Migration):
    replaces = [
        ("fonts", "0001_squashed_0007_auto_20190517_1907"),
        ("fonts", "0002_auto_20210512_1955"),
        ("fonts", "0003_alter_fontgroup_unique_together_and_more"),
    ]

    initial = True

    dependencies = [
        ("trans", "0001_squashed_weblate_5"),
        ("lang", "0001_squashed_weblate_5"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Font",
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
                    "family",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Font family"
                    ),
                ),
                (
                    "style",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Font style"
                    ),
                ),
                (
                    "font",
                    models.FileField(
                        help_text="OpenType and TrueType fonts are supported.",
                        storage=django.core.files.storage.FileSystemStorage(
                            location=data_dir("fonts")
                        ),
                        upload_to="",
                        validators=[weblate.fonts.validators.validate_font],
                        verbose_name="Font file",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="trans.project"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("family", "style", "project")},
                "verbose_name": "Font",
                "verbose_name_plural": "Fonts",
            },
            bases=(models.Model, weblate.trans.mixins.UserDisplayMixin),
        ),
        migrations.CreateModel(
            name="FontGroup",
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
                    "name",
                    models.SlugField(
                        help_text="Identifier you will use in checks to select this font group. Avoid whitespaces and special characters.",
                        max_length=100,
                        verbose_name="Font group name",
                    ),
                ),
                (
                    "font",
                    models.ForeignKey(
                        help_text="Default font is used unless per language override matches.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fonts.font",
                        verbose_name="Default font",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        db_index=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trans.project",
                    ),
                ),
            ],
            options={
                "unique_together": {("project", "name")},
                "verbose_name": "Font group",
                "verbose_name_plural": "Font groups",
            },
        ),
        migrations.CreateModel(
            name="FontOverride",
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
                    "font",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fonts.font",
                        verbose_name="Font",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        db_index=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fonts.fontgroup",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lang.language",
                        verbose_name="Language",
                    ),
                ),
            ],
            options={
                "unique_together": {("group", "language")},
                "verbose_name": "Font override",
                "verbose_name_plural": "Font overrides",
            },
        ),
    ]
