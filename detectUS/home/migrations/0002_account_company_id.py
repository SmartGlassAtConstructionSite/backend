# Generated by Django 4.0.5 on 2022-07-24 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='company_id',
            field=models.ForeignKey(db_column='company_id', default='', on_delete=django.db.models.deletion.CASCADE, to='home.company'),
        ),
    ]
