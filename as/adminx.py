from .models import *
import xadmin
class IrsBusinessContactAPP(object):
    list_display = ['business_id','user_type','user_name','contact_type','contact_no','contact_status','contype_flag']
    search_fields = ['business_id','user_type','user_name','contact_type','contact_no','contact_status','contype_flag']
    list_filter = ['business_id','user_type','user_name','contact_type','contact_no','contact_status','contype_flag']
    list_editable =['business_id','user_type','user_name','contact_type','contact_no','contact_status','contype_flag']
    refresh_times = [2, 4]
xadmin.site.register(IrsBusinessContact, IrsBusinessContactAPP)
class IrsBusinessUserAPP():
    list_display =['business_id','user_type','user_name','mobile_phone','user_wxid','user_address','user_status','certificate_id','user_birthday','user_bal','user_adviser','user_spread','register_date','exceed_date','contype_flag','snode']
    search_fields = ['business_id', 'user_type', 'user_name', 'mobile_phone', 'user_wxid', 'user_address', 'user_status',
                    'certificate_id', 'user_birthday', 'user_bal', 'user_adviser', 'user_spread', 'register_date',
                    'exceed_date', 'contype_flag', 'snode']
    list_filter = ['business_id', 'user_type', 'user_name', 'mobile_phone', 'user_wxid', 'user_address', 'user_status',
                    'certificate_id', 'user_birthday', 'user_bal', 'user_adviser', 'user_spread', 'register_date',
                    'exceed_date', 'contype_flag', 'snode']
    list_editable = ['business_id', 'user_type', 'user_name', 'mobile_phone', 'user_wxid', 'user_address', 'user_status',
                    'certificate_id', 'user_birthday', 'user_bal', 'user_adviser', 'user_spread', 'register_date',
                    'exceed_date', 'contype_flag', 'snode']
    refresh_times = [2, 4]
xadmin.site.register(IrsBusinessUser, IrsBusinessUserAPP)
class IrsYwtyDictAPP():
    list_display =['dict_name','dict_code','dict_target','dict_default','dict_snote']
    search_fields = ['dict_name', 'dict_code', 'dict_target', 'dict_default', 'dict_snote']
    list_filter = ['dict_name', 'dict_code', 'dict_target', 'dict_default', 'dict_snote']
    list_editable =['dict_name', 'dict_code', 'dict_target', 'dict_default', 'dict_snote']
    refresh_times = [2, 4]
xadmin.site.register(IrsYwtyDict, IrsYwtyDictAPP)
class IrsBusinessInfoAPP():
    list_display=['business_id','business_name','business_type','business_rule','business_scope','business_address','business_person',
                  'business_contact','business_status','register_time','register_user','modify_time','modify_user','snote']
    search_fields = ['business_id', 'business_name', 'business_type', 'business_rule', 'business_scope',
                    'business_address', 'business_person',
                    'business_contact', 'business_status', 'register_time', 'register_user', 'modify_time',
                    'modify_user', 'snote']
    list_filter = ['business_id', 'business_name', 'business_type', 'business_rule', 'business_scope',
                    'business_address', 'business_person',
                    'business_contact', 'business_status', 'register_time', 'register_user', 'modify_time',
                    'modify_user', 'snote']
    list_editable= ['business_id', 'business_name', 'business_type', 'business_rule', 'business_scope',
                    'business_address', 'business_person',
                    'business_contact', 'business_status', 'register_time', 'register_user', 'modify_time',
                    'modify_user', 'snote']
    refresh_times = [2, 4]
xadmin.site.register(IrsBusinessInfo,IrsBusinessInfoAPP)
from xadmin import views
class GlobalSettings(object):
    site_title="爱如生管理系统"#后台名称
    site_footer="irusheng"#页脚版权
xadmin.site.register(views.CommAdminView,GlobalSettings)

