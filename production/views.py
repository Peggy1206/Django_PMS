from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import DailyRecord, Raw_Material,product,addMaterial
from .admin import DailyRecordAdmin
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.db.models import F
# from docutils.parsers import null
from django.db.models import Sum
from django import forms
import datetime
import math
# Create your views here.

# def historyrecord(request):
#     return render(request,'historyrecord.html')
# def inventory(request):
#     return render(request,'inventory.html')
# def create_inventory(request):
#     return render(request,'create_inventory.html')
# def material(request):
#     return render(request,'material.html')

def inventory(request):
    
    use_list = Raw_Material.objects.all().order_by('m_number')
    
    class Meta:
        model = Raw_Material
        fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory',]
    return render(request,'inventory.html', locals())

def historyrecord(request):           #歷史紀錄，按照日期排序
    # drecord_list = DailyRecord.objects.all().order_by('-sell_date')
    # return render(request,'historyrecord.html', locals())
    query = request.GET.get('search_res', None)
    context = {}

    class Meta:
        model = DailyRecord
        fields = ['sell_date', 'sell_pd1','sell_pd2','sell_pd3','sell_pd4','sell_pd5', ]

    if query and request.method == 'GET':
        results = DailyRecord.objects.filter(sell_date=query)
        context.update({'results': results})
    
    return render(request,'historyrecord.html',context)

#def CalculateTodayConsume(request):


# def CountUseAmount(request):
#     result = DailyRecord.objects.all().annotate(prod=F('sell_pd1') * F('blacktea'))

class TodaySellForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ['sell_date', 'sell_pd1','sell_pd2','sell_pd3','sell_pd4','sell_pd5', ]               


    

# def material(request):
#     drecord_list = DailyRecord.objects.all().order_by('-sell_date')
#     for d in drecord_list:
#         spring_predictsell = d.filter(date__range=["2019-01-01", "2019-03-31"])

#     return render(request,'material.html',locals())

def material(request):                             #讓使用者查詢，並列出預測的量
     
    query = request.GET.get('search_res', None)
    context = {}
    class Meta:
        model = DailyRecord
        fields = ['sell_date', 'sell_pd1','sell_pd2','sell_pd3','sell_pd4','sell_pd5', ]

    if query and request.method == 'GET':
        results = DailyRecord.objects.filter(sell_date=query)
        context.update({'results': results})

        # spring_start_date = datetime.date(2019, 1, 1)                  #春天的銷量
        # spring_end_date =  datetime.date(2019, 3, 31) 
        # DailyRecord.sell_date.strftime('%Y-%m-%d')
        # spring = DailyRecord.objects.filter(sell_date=[spring_start_date, spring_end_date])
        for r in results:  
                r.predicted_sell＿pd1 =math.ceil((r.sell_pd1)* 0.9)     #冬天的預測量
                r.predicted_sell＿pd2 =math.ceil((r.sell_pd2)* 1.1)
                r.predicted_sell＿pd3 =math.ceil((r.sell_pd3)* 1.2)
                r.predicted_sell＿pd4 =math.ceil((r.sell_pd4)* 0.9)
                r.predicted_sell＿pd5 =math.ceil((r.sell_pd5)* 0.8)
                
                r.predicted_blacktea_usage = math.ceil(r.sell_pd1 + r.sell_pd2 + r.sell_pd3 )*300
                r.predicted_milk_usage = math.ceil(r.sell_pd1 + r.sell_pd2 + r.sell_pd3 + r.sell_pd4 + r.sell_pd5 )*200
                r.predicted_pearl_usage = math.ceil(r.sell_pd3 + r.sell_pd5 )*20
                r.predicted_taro_usage = math.ceil(r.sell_pd2)*20
                r.predicted_honey_usage = math.ceil(r.sell_pd4 + r.sell_pd5 )*100

                r.predicted_blacktea_unit = round(((r.sell_pd1 + r.sell_pd2 + r.sell_pd3 )*300/30000),1)
                r.predicted_milk_unit = round(((r.sell_pd1 + r.sell_pd2 + r.sell_pd3 + r.sell_pd4 + r.sell_pd5 )*200/5000),2)
                r.predicted_pearl_unit = round(((r.sell_pd3 + r.sell_pd5 )*20/3000),2)
                r.predicted_taro_unit = round(((r.sell_pd2)*20/3000),2)
                r.predicted_honey_unit = round(((r.sell_pd4 + r.sell_pd5 )*100/3000),2)

        use_list = Raw_Material.objects.all().order_by('m_number')
    
    class Meta:
        model = Raw_Material
        fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory',]
        
        # Matirial.objects.all().filter(m_name='紅茶（ml）').update(m_left_amount=F('m_left_amount')/30000)
        # for a in use_list:
        #     a.predictday_blacktea = math.ceil((a.m_left_amount - a.m_safe_inventory)/r.predicted_blacktea_usage)
    return render(request,'material.html', locals())

#     class Meta:
#         model = Raw_Material
#         fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory',]
#         use_list = Raw_Material.objects.all().order_by('m_number')
#         for a in use_list:
#             a.predictday_blacktea = math.ceil((a.m_left_amount - a.m_safe_inventory)/r.predicted_blacktea_usage)
#     return render(request,'material.html', locals())

class CurrentUseForm(HttpResponseRedirect):
    class Meta:
        model =Raw_Material
        fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory']
        latest_record = DailyRecord.objects.latest('id')
        used_blacktea= (latest_record.sell_pd1 + latest_record.sell_pd2 + latest_record.sell_pd3 )*300
        Raw_Material.objects.all().filter(m_name='紅茶（ml）').update(m_left_amount=F('m_left_amount') - used_blacktea)
        
        
        used_milk =(latest_record.sell_pd1 + latest_record.sell_pd2 + latest_record.sell_pd3 + latest_record.sell_pd4 + latest_record.sell_pd5)*200
        Raw_Material.objects.all().filter(m_name='牛奶（ml）').update(m_left_amount=F('m_left_amount') - used_milk)
        
        used_pearl =(latest_record.sell_pd3 + latest_record.sell_pd5)*20
        Raw_Material.objects.all().filter(m_name='珍珠（g）').update(m_left_amount=F('m_left_amount') - used_pearl)
        
        used_taro =(latest_record.sell_pd2)*20
        Raw_Material.objects.all().filter(m_name='芋圓（g）').update(m_left_amount=F('m_left_amount') - used_taro)
        
        used_honey =(latest_record.sell_pd4 + latest_record.sell_pd5)*100
        Raw_Material.objects.all().filter(m_name='蜂蜜（g）').update(m_left_amount=F('m_left_amount') - used_honey)
         
class AddUseForm(HttpResponseRedirect):
    class Meta:
        model = Raw_Material
        fields = ['m_number', 'm_name','m_left_amount','m_safe_inventory']
        latest_add_record = addMaterial.objects.latest('add_date')

        new_blacktea= latest_add_record.add_blacktea*30000 
        Raw_Material.objects.all().filter(m_name='紅茶（ml）').update(m_left_amount=F('m_left_amount') + new_blacktea)

        new_milk = latest_add_record.add_milk*5000
        Raw_Material.objects.all().filter(m_name='牛奶（ml）').update(m_left_amount=F('m_left_amount') + new_milk)
        
        new_pearl = latest_add_record.add_pearl*3000
        Raw_Material.objects.all().filter(m_name='珍珠（g）').update(m_left_amount=F('m_left_amount') + new_pearl)

        new_taro = latest_add_record.add_taro*3000
        Raw_Material.objects.all().filter(m_name='芋圓（g）').update(m_left_amount=F('m_left_amount') + new_taro)
        
        new_honey =latest_add_record.add_honey*3000
        Raw_Material.objects.all().filter(m_name='蜂蜜（g）').update(m_left_amount=F('m_left_amount') + new_honey)
