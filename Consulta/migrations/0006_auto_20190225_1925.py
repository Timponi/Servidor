# Generated by Django 2.1.7 on 2019-02-25 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consulta', '0005_auto_20190225_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='hist_trafoa',
            name='DataFim',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hist_trafoa',
            name='dataInicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]