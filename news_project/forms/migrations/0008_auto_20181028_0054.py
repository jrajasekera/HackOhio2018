# Generated by Django 2.1 on 2018-10-28 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_sortby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sortby',
            name='id',
        ),
        migrations.AlterField(
            model_name='sortby',
            name='displaySortBy',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
