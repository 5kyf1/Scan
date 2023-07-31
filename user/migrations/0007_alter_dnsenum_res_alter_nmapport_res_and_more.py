# Generated by Django 4.1.4 on 2022-12-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_case_ip_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dnsenum",
            name="res",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="nmapport",
            name="res",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="sslcertificate",
            name="res",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subdomain",
            name="res",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="wappalyzermodel",
            name="res",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="whatcms",
            name="res",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="whois",
            name="res",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
