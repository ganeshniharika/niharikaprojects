# Generated by Django 2.1.7 on 2019-03-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieportalapp', '0002_bookdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='m_time',
            field=models.CharField(max_length=20),
        ),
    ]
