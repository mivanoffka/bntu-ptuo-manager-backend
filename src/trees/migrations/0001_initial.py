# Generated by Django 5.1.7 on 2025-05-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BntuDepartmentModel',
            fields=[
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=255, unique=True)),
                ('label', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'bntu_departments',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TradeUnionDepartmentModel',
            fields=[
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=255, unique=True)),
                ('label', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'trade_union_departments',
                'abstract': False,
            },
        ),
    ]
