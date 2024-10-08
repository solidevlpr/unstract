# Generated by Django 4.2.1 on 2024-02-28 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("prompt_profile_manager", "0006_alter_profilemanager_x2text"),
        ("prompt_studio_core", "0004_customtool_summarize_as_source_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customtool",
            name="default_profile",
            field=models.ForeignKey(
                blank=True,
                db_comment="Default LLM Profile used in prompt",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="default_profile",
                to="prompt_profile_manager.profilemanager",
            ),
        ),
        migrations.AlterField(
            model_name="customtool",
            name="summarize_as_source",
            field=models.BooleanField(
                db_comment="Flag to use summarized content as source",
                default=True,
            ),
        ),
        migrations.AlterField(
            model_name="customtool",
            name="summarize_context",
            field=models.BooleanField(
                db_comment="Flag to summarize content", default=True
            ),
        ),
        migrations.AlterField(
            model_name="customtool",
            name="summarize_llm_profile",
            field=models.ForeignKey(
                blank=True,
                db_comment="LLM Profile used for summarize",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="summarize_llm_profile",
                to="prompt_profile_manager.profilemanager",
            ),
        ),
    ]
