# Generated by Django 2.1 on 2018-10-28 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_country_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Sort',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
    ]