# Generated by Django 4.0.5 on 2022-07-20 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0002_alter_building_table_alter_company_table'),
        ('home', '0006_account_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='company_id',
            field=models.ForeignKey(db_column='company_id', default='', on_delete=django.db.models.deletion.CASCADE, to='listapp.company'),
        ),
    ]
