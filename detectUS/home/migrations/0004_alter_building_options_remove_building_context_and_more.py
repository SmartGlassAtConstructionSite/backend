# Generated by Django 4.0.5 on 2022-07-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_glass_building_id_glass_company_id_glass_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={},
        ),
        migrations.RemoveField(
            model_name='building',
            name='context',
        ),
        migrations.AddField(
            model_name='building',
            name='builing_context',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='building',
            name='building_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='building',
            name='building_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]