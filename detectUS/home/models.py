from csv import unregister_dialect
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import CASCADE
from curses import REPORT_MOUSE_POSITION


class Account(models.Model):
    user_id = models.CharField(max_length=45, null=False, primary_key=True)
    user_pw = models.CharField(max_length=20, null=False)
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE, default='', db_column='company_id')
    is_admin = models.IntegerField(null=False, default='0')
    name = models.CharField(max_length=45, null=False, default='')

    class Meta:
        db_table = 'account'


class Glass(models.Model):
    glass_id = models.AutoField(null=False,primary_key=True)
    glass_name = models.CharField(max_length=45,null=False)
    user_id = models.CharField(max_length=45,null=True)
    building_id = models.IntegerField(null=True)
    company_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'glass'


class Raw_data(models.Model): # 사용 X
    raw_data_id = models.AutoField(primary_key=True)
    picture = models.CharField(max_length=200,null=True)
    voice = models.CharField(max_length=100,null=True)
    voice_to_text = models.CharField(max_length=100,null=True)
    upload_user_id = models.CharField(max_length=45,null=True)
    upload_target_building_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'raw_data'


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=64)

    class Meta:
        db_table = 'company'


class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=45, null=False)
    company_id = models.ForeignKey(Company, on_delete=CASCADE, db_column='company_id')  # 외래키 지정
    max_floor = models.IntegerField(null=True)
    min_floor = models.IntegerField(null=True)
    building_context = models.CharField(default='',max_length=100)

    class Meta:
        db_table = 'building'


class Issue(models.Model): # 사용 X
    issue_id = models.AutoField(primary_key=True)
    raw_data_id = models.OneToOneField("Raw_data",on_delete=models.CASCADE, db_column='raw_data_id',default='')
    floor = models.CharField(max_length=10,null=True)
    room = models.CharField(max_length=100,null=True)
    details = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'issue'


class Floor(models.Model): # 설계도
    floor = models.IntegerField(null=False)
    building_id = models.ForeignKey("Building", on_delete=models.CASCADE, db_column='building_id', default='')
    drawing = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = 'floor'
        unique_together = (("floor", "building_id"),)  # composite primary key


class Image(models.Model): # 이미지
    image_url = models.CharField(max_length=200,null=True)
    upload_user_id = models.CharField(max_length=45,null=True)
    upload_target_building_id = models.IntegerField(null=True)
    key_value = models.CharField(max_length=200,null=True)
    
    class Meta:
        db_table = 'image'

class Voice_to_Text(models.Model): # 음성파일
    voice_to_text = models.CharField(max_length=200,null=True)
    upload_user_id = models.CharField(max_length=45,null=True)
    upload_target_building_id = models.IntegerField(null=True)
    key_value = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = 'voice_to_text'

class Key_Table(models.Model): # 음성, 이미지 연결 키
    user_id = models.ForeignKey(Account, on_delete=CASCADE, db_column='user_id')
    key_value = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = 'key_table'