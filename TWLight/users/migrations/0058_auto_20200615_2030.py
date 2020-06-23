# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-15 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0057_expire_all_sessions")]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="lang",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ar", "العربية"),
                    ("br", "brezhoneg"),
                    ("da", "dansk"),
                    ("de", "Deutsch"),
                    ("en", "English"),
                    ("en-gb", "British English"),
                    ("eo", "Esperanto"),
                    ("es", "español"),
                    ("fa", "فارسی"),
                    ("fi", "suomi"),
                    ("fr", "français"),
                    ("hi", "हिन्दी"),
                    ("ja", "日本語"),
                    ("ko", "한국어"),
                    ("mk", "македонски"),
                    ("mr", "मराठी"),
                    ("my", "မြန်မာဘာသာ"),
                    ("pt", "português"),
                    ("pt-br", "português do Brasil"),
                    ("ro", "română"),
                    ("ru", "русский"),
                    ("sv", "svenska"),
                    ("ta", "தமிழ்"),
                    ("tr", "Türkçe"),
                    ("uk", "українська"),
                    ("vi", "Tiếng Việt"),
                    ("zh-hans", "中文（简体）"),
                    ("zh-hant", "中文（繁體）"),
                ],
                help_text="Language",
                max_length=128,
                null=True,
            ),
        )
    ]