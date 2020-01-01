# Generated by Django 3.0.1 on 2019-12-29 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pd_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pd_name', models.CharField(max_length=20)),
                ('pd_price', models.IntegerField()),
                ('blackTea', models.IntegerField(default=0)),
                ('milk', models.IntegerField(default=0)),
                ('pearl', models.IntegerField(default=0)),
                ('taro', models.IntegerField(default=0)),
                ('honey', models.IntegerField(default=0)),
            ],
        ),
    ]
