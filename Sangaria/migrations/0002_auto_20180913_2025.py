# Generated by Django 2.0 on 2018-09-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sangaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='visitors',
            name='Telephone',
            field=models.IntegerField(),
        ),
    ]
