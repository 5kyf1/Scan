# Generated by Django 4.1.4 on 2023-03-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_imageanalysis'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseSearchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(max_length=5, unique=True)),
            ],
        ),
    ]
