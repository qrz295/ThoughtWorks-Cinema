# Generated by Django 2.0.1 on 2018-01-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cinema_Pages', '0009_auto_20180113_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
    ]