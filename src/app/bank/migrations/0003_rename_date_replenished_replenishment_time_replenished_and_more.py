# Generated by Django 4.1.1 on 2022-09-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replenishment',
            old_name='date_replenished',
            new_name='time_replenished',
        ),
        migrations.RenameField(
            model_name='transfer',
            old_name='date_transfered',
            new_name='time_transfered',
        ),
        migrations.AlterField(
            model_name='customer',
            name='fname',
            field=models.CharField(max_length=255, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lname',
            field=models.CharField(max_length=255, verbose_name='Second name'),
        ),
    ]
