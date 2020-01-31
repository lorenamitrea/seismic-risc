# Generated by Django 2.2.4 on 2019-11-13 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("map_app", "0013_auto_20191113_2105")]

    operations = [
        migrations.AlterField(
            model_name="building",
            name="certified_expert",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="building",
            name="height_regime",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="building",
            name="land_registry_number",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="building",
            name="observations",
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
