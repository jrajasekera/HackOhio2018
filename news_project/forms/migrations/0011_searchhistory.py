# Generated by Django 2.1 on 2018-10-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0010_auto_20181028_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=30)),
                ('sortBy', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=30)),
            ],
        ),
    ]
