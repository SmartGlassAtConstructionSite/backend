# Generated by Django 4.0.5 on 2022-07-24 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_building_options_remove_building_context_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='floor',
            name='building_id',
            field=models.ForeignKey(db_column='building_id', default='', on_delete=django.db.models.deletion.CASCADE, to='home.building'),
        ),
        migrations.AddField(
            model_name='issue',
            name='building_id',
            field=models.ForeignKey(db_column='building_id', default='', on_delete=django.db.models.deletion.CASCADE, to='home.building'),
        ),
        migrations.AddField(
            model_name='issue',
            name='raw_data_id',
            field=models.OneToOneField(db_column='raw_data_id', default='', on_delete=django.db.models.deletion.CASCADE, to='home.raw_data'),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='drawing_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='floor',
            unique_together={('floor', 'building_id')},
        ),
    ]