# Generated by Django 2.1.7 on 2019-03-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieportalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.IntegerField()),
                ('m_name', models.CharField(max_length=100)),
                ('m_time', models.TimeField()),
                ('m_theatre', models.CharField(max_length=100)),
            ],
        ),
    ]
