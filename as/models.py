from django.db import models

# Create your models here.
class IrsBusinessInfo(models.Model):
    contact_choices = (('0', u'待审核'), ('1', '正常'), ('2', u'暂停'), ('3', u'失效'))
    business_id = models.CharField(db_column='BUSINESS_ID', primary_key=True, max_length=9,verbose_name="商户ID")  # Field name made lowercase.
    business_name = models.CharField(db_column='BUSINESS_NAME', max_length=120, blank=True, null=True,verbose_name="商户名称")  # Field name made lowercase.
    business_type = models.CharField(db_column='BUSINESS_TYPE', max_length=5, blank=True, null=True,verbose_name="商户类型")#参照数据字典表配置 select * from irs_ywty_dict where dict_name='BUSINESS_TYPE'  # Field name made lowercase.
    business_rule = models.CharField(db_column='BUSINESS_RULE', max_length=10, blank=True, null=True,verbose_name="商户权限")  # Field name made lowercase.
    business_scope = models.CharField(db_column='BUSINESS_SCOPE', max_length=200, blank=True, null=True,verbose_name="商户经营范围")  # Field name made lowercase.
    business_address = models.CharField(db_column='BUSINESS_ADDRESS', max_length=200, blank=True, null=True,verbose_name="商户地址")  # Field name made lowercase.
    business_person = models.CharField(db_column='BUSINESS_PERSON', max_length=10, blank=True, null=True,verbose_name="负责人名称")  # Field name made lowercase.
    business_contact = models.CharField(choices=contact_choices,db_column='BUSINESS_CONTACT', max_length=11, blank=True, null=True,verbose_name="商户状态")#0-录入待审核 1-正常2-暂停3-失效  # Field name made lowercase.
    business_status = models.CharField(db_column='BUSINESS_STATUS', max_length=1, blank=True, null=True,verbose_name="经营状况")  # Field name made lowercase.
    register_time = models.DateTimeField(db_column='REGISTER_TIME', blank=True, null=True,verbose_name="注册时间")  # Field name made lowercase.
    register_user = models.CharField(db_column='REGISTER_USER', max_length=10, blank=True, null=True,verbose_name="注册人")  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='MODIFY_TIME', blank=True, null=True,verbose_name="修改时间")  # Field name made lowercase.
    modify_user = models.CharField(db_column='MODIFY_USER', max_length=10, blank=True, null=True,verbose_name="修改人")  # Field name made lowercase.
    snote = models.CharField(db_column='SNOTE', max_length=200, blank=True, null=True,verbose_name="备注")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IRS_BUSINESS_INFO'
        verbose_name_plural="商户信息表"
class IrsBusinessContact(models.Model):
    type_choices=(('001',u'企业法人'),('002',u'财务人员'),('003',u'客服人员'),('004','售后人员'))
    contact_choices=(('01',u'手机号码'),('02',u'短信'),('03',u'微信号'),('04','QQ号'),('05','邮箱'))
    status_choices=(('0',u'待确定'),('1','正常'),('2',u'暂停'),('3',u'撤销'))
    flag_choices=(('0',u'不需要通知'),('1',u'需要通知'))
    business_id = models.CharField(db_column='BUSINESS_ID', primary_key=True, max_length=9,verbose_name="商户ID")  # Field name made lowercase.
    user_type = models.CharField(choices=type_choices,db_column='USER_TYPE', max_length=3, blank=True, null=True,verbose_name="联系人类型")  #001-企业法人 002-财务人员 003-客服人员  004-售后人员 # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=10, blank=True, null=True,verbose_name="联系人姓名")  # Field name made lowercase.
    contact_type = models.CharField(choices=contact_choices,db_column='CONTACT_TYPE', max_length=2, blank=True, null=True,verbose_name="联系方式")  #01-手机号码 02-短信03-微信号04-QQ号05-邮箱 # Field name made lowercase.
    contact_no = models.CharField(db_column='CONTACT_NO', max_length=30,verbose_name="微信号码")  # Field name made lowercase.
    contact_status = models.CharField(choices=status_choices,db_column='CONTACT_STATUS', max_length=1, blank=True, null=True,verbose_name="商户状态")#0-初始待确认 1-正常2-暂停 3-撤销  # Field name made lowercase.
    contype_flag = models.CharField(choices=flag_choices,db_column='CONTYPE_FLAG', max_length=1, blank=True, null=True,verbose_name="通知状态") #0-不需要通知1-需要通知 # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IRS_BUSINESS_CONTACT'
        unique_together = (('business_id', 'contact_no'),)
        verbose_name_plural="商户信息"

class IrsBusinessUser(models.Model):
    status_choices = (('0', u'待确定'), ('1', '正常'), ('2', u'暂停'), ('3', u'撤销'))
    flag_choices = (('0', u'不需要通知'), ('1', u'需要通知'))
    business_id = models.CharField(db_column='BUSINESS_ID', primary_key=True, max_length=9,verbose_name="商户ID")  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=15, blank=True, null=True,verbose_name="会员等级")#会员等级之类的各商户可自己个性化定义 在数据字典中，用“商户号9位”+“自定义”存放在dict_code字段中  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=50, blank=True, null=True,verbose_name="会员名称")  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=11, blank=True, null=True,verbose_name="手机号码")  # Field name made lowercase.
    user_wxid = models.CharField(db_column='USER_WXID', max_length=30,verbose_name="微信号码")  # Field name made lowercase.
    user_address = models.CharField(db_column='USER_ADDRESS', max_length=200, blank=True, null=True,verbose_name="联系地址")  # Field name made lowercase.
    user_status = models.CharField(choices=status_choices,db_column='USER_STATUS', max_length=1, blank=True, null=True,verbose_name="会员状态")#0-初始待确认 1-正常2-暂停 3-撤销  # Field name made lowercase.
    certificate_id = models.CharField(db_column='CERTIFICATE_ID', max_length=18, blank=True, null=True,verbose_name="身份证号")  # Field name made lowercase.
    user_birthday = models.DateField(db_column='USER_BIRTHDAY', blank=True, null=True,verbose_name="会员生日")  # Field name made lowercase.
    user_bal = models.DecimalField(db_column='USER_BAL', max_digits=16, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    user_adviser = models.CharField(db_column='USER_ADVISER', max_length=50, blank=True, null=True,verbose_name="办卡人员")  # Field name made lowercase.
    user_spread = models.CharField(db_column='USER_SPREAD', max_length=50, blank=True, null=True,verbose_name="推荐人")  # Field name made lowercase.
    register_date = models.DateField(db_column='REGISTER_DATE', blank=True, null=True,verbose_name="办卡日期")  # Field name made lowercase.
    exceed_date = models.DateField(db_column='EXCEED_DATE', blank=True, null=True,verbose_name="过期日期")  # Field name made lowercase.
    contype_flag = models.CharField(choices=flag_choices,db_column='CONTYPE_FLAG', max_length=1, blank=True, null=True,verbose_name="通知状态")  #0-不需要通知1-需要通知 # Field name made lowercase.
    snode = models.CharField(db_column='SNODE', max_length=200, blank=True, null=True,verbose_name="备注")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IRS_BUSINESS_USER'
        unique_together = (('business_id', 'user_wxid'),)
        verbose_name_plural="商户会员表"
class IrsYwtyDict(models.Model):
    dict_name = models.CharField(db_column='DICT_NAME', primary_key=True, max_length=50,verbose_name="字典名称")  # Field name made lowercase.
    dict_code = models.CharField(db_column='DICT_CODE', max_length=50,verbose_name="字典键值")  # Field name made lowercase.
    dict_target = models.CharField(db_column='DICT_TARGET', max_length=50, blank=True, null=True,verbose_name="对应解释")  # Field name made lowercase.
    dict_default = models.CharField(db_column='DICT_DEFAULT', max_length=1, blank=True, null=True,verbose_name="默认转换")  # Field name made lowercase.
    dict_snote = models.CharField(db_column='DICT_SNOTE', max_length=200, blank=True, null=True,verbose_name="字典说明")  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'IRS_YWTY_DICT'
        unique_together = (('dict_name', 'dict_code'),)
        verbose_name_plural="通用字典表"

