# Generated by Django 5.0.7 on 2024-09-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_alter_drinks_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=100),
        ),
    ]
