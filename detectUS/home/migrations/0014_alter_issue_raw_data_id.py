# Generated by Django 4.0.5 on 2022-09-09 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_merge_20220830_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='raw_data_id',
            field=models.OneToOneField(db_column='raw_data_id', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='home.raw_data'),
        ),
    ]
