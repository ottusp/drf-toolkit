# Generated by Django 3.2.11 on 2022-01-18 14:00

from django.db import migrations, models
import django.db.models.deletion
import drf_kit.models.diff_models
import drf_kit.models.file_models


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tale",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="updated at")),
                ("deleted_at", models.DateTimeField(blank=True, default=None, null=True, verbose_name="deleted at")),
                (
                    "order",
                    models.PositiveIntegerField(
                        blank=True, db_index=True, default=None, null=True, verbose_name="order"
                    ),
                ),
                ("type", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
            options={
                "ordering": ("order", "-updated_at"),
                "get_latest_by": "updated_at",
                "abstract": False,
            },
            bases=(
                drf_kit.models.diff_models.ModelDiffMixin,
                drf_kit.models.file_models.BoundedFileMixin,
                models.Model,
            ),
        ),
        migrations.AddIndex(
            model_name="triwizardplacement",
            index=models.Index(fields=["order"], name="test_app_tr_order_1c9299_idx"),
        ),
        migrations.CreateModel(
            name="DarkTale",
            fields=[
                (
                    "tale_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="test_app.tale",
                    ),
                ),
                ("dark_level", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ("order", "-updated_at"),
                "get_latest_by": "updated_at",
                "abstract": False,
            },
            bases=("test_app.tale",),
        ),
        migrations.CreateModel(
            name="HappyTale",
            fields=[
                (
                    "tale_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="test_app.tale",
                    ),
                ),
                ("laugh_level", models.IntegerField(default=0)),
            ],
            options={
                "ordering": ("order", "-updated_at"),
                "get_latest_by": "updated_at",
                "abstract": False,
            },
            bases=("test_app.tale",),
        ),
        migrations.AddIndex(
            model_name="tale",
            index=models.Index(fields=["deleted_at"], name="test_app_ta_deleted_5e3327_idx"),
        ),
        migrations.AddIndex(
            model_name="tale",
            index=models.Index(fields=["order"], name="test_app_ta_order_73d8cf_idx"),
        ),
        migrations.AddIndex(
            model_name="tale",
            index=models.Index(fields=["updated_at"], name="test_app_ta_updated_0044f7_idx"),
        ),
    ]