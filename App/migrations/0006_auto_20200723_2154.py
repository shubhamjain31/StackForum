# Generated by Django 3.0.3 on 2020-07-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20200723_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='questionId',
            field=models.UUIDField(default='7a17364d592a45d9a64aee502e67d933', unique=True),
        ),
    ]