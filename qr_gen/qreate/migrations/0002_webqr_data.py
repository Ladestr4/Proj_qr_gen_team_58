# Generated by Django 4.0.6 on 2022-07-28 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qreate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webqr',
            name='data',
            field=models.CharField(default='o', max_length=400),
            preserve_default=False,
        ),
    ]
