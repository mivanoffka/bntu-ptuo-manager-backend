# Generated by Django 5.1.7 on 2025-06-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employeeversionmodel_exemptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeversionmodel',
            name='middle_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
