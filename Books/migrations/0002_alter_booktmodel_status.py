# Generated by Django 4.0.6 on 2022-08-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktmodel',
            name='status',
            field=models.CharField(default='AVAILABLE', max_length=20),
        ),
    ]
