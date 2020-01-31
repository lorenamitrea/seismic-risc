# Generated by Django 2.2.3 on 2019-07-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("map_app", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Building",
            fields=[
                (
                    "id_general",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("clasa_categorie", models.CharField(max_length=5)),
                ("nr_pmb", models.IntegerField()),
                ("lat", models.FloatField()),
                ("long", models.FloatField()),
                ("loc", models.CharField(max_length=60)),
                ("adresa", models.CharField(max_length=250)),
                ("nr_postal", models.CharField(max_length=8)),
                ("sector", models.CharField(default="sector", max_length=20)),
                ("nr_sector", models.IntegerField()),
                ("regim_inaltime", models.CharField(max_length=50)),
                ("nr_apart", models.IntegerField()),
                ("arie_desfasurata", models.FloatField()),
                ("an_expertiza", models.IntegerField()),
                ("expert_atestat", models.CharField(max_length=100)),
                ("obs", models.CharField(max_length=1000)),
                ("numar_cadastral", models.IntegerField()),
                ("nr_carte_funciara", models.CharField(max_length=50)),
                ("actualizare_pmb", models.DateField()),
                ("editare_admin", models.DateField()),
            ],
        ),
        migrations.RenameModel(old_name="FileModel", new_name="CsvFile"),
    ]
