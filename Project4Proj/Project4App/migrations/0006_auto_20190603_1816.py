# Generated by Django 2.2 on 2019-06-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project4App', '0005_auto_20190603_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
