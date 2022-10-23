# Generated by Django 4.1.1 on 2022-10-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_replenishment_negative_amount_replenishment'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='transfer',
            constraint=models.CheckConstraint(check=models.Q(('amount__gte', 0)), name='negative_amount_transfer'),
        ),
        migrations.AddConstraint(
            model_name='transfer',
            constraint=models.CheckConstraint(check=models.Q(('from_account__exact', models.F('to_account')), _negated=True), name='same_account_transfer'),
        ),
    ]
