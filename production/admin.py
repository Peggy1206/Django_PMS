from django.contrib import admin
from .models import Raw_Material,product, DailyRecord, addMaterial
# Register your models here.

admin.site.register(Raw_Material)


class DailyRecordAdmin(admin.ModelAdmin):    #記載每天的銷量
    list_display=('sell_date','sell_pd1','sell_pd2','sell_pd3','sell_pd4','sell_pd5')
    list_filter=('sell_date','sell_pd1','sell_pd2','sell_pd3','sell_pd4','sell_pd5')
    #ordering=('sell_date')
    #search_fields=('sell_date')
admin.site.register(DailyRecord,DailyRecordAdmin)

class Product(admin.ModelAdmin):     #記載每種品項有多少原料
    list_display = ('pd_id','pd_name','pd_price','blackTea','milk','pearl','taro','honey')
admin.site.register(product,Product)

class AddMaterial(admin.ModelAdmin):
    list_display = ('add_date','add_blacktea','add_milk','add_pearl','add_taro','add_honey',)
admin.site.register(addMaterial,AddMaterial)