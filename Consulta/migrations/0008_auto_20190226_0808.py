# Generated by Django 2.1.7 on 2019-02-26 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Consulta', '0007_auto_20190225_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hist_trafoa',
            old_name='E3TimeStamp',
            new_name='Data',
        ),
    ]
