# Generated by Django 4.0.5 on 2022-07-24 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_account_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='glass',
            name='building_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='glass',
            name='company_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='glass',
            name='user_id',
            field=models.CharField(max_length=45, null=True),
        ),
    ]