# Generated by Django 2.0.4 on 2018-07-07 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20180707_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='registration_date',
            field=models.DateField(blank=True, null=True, verbose_name='fecha de alta'),
        ),
    ]
