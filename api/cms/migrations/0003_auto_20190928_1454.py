# Generated by Django 2.2.4 on 2019-09-28 14:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("cms", "0002_attachment")]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="content",
            field=ckeditor.fields.RichTextField(),
        )
    ]
