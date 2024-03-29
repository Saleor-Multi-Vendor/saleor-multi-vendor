# Generated by Django 3.2.2 on 2021-08-10 11:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("warehouse", "0014_remove_warehouse_company_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendor",
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
                ("shop_name", models.CharField(max_length=256)),
                (
                    "allocation",
                    models.ManyToManyField(
                        related_name="vendor", to="warehouse.Allocation"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vendor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "warehouse",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="vendor",
                        to="warehouse.warehouse",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vendor",
                "verbose_name_plural": "Vendors",
                "permissions": (("manage_vendor", "Manage Vendor."),),
            },
        ),
    ]
