from django.shortcuts import render
from django.db.models import Count
from django.db.models import Q
from . import models
from marketing.models import Customer
from marketing.models import Item,PurRecord
# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return render(request,'index.html')
def member(request):
    boy = Customer.objects.filter(c_sex = 1)
    #boy = Customer.c_sex.filter(c_sex = 1)
    numB = len(boy)
    girl = Customer.objects.filter(c_sex = 2)
    numG = len(girl)

    CusList = Customer.objects.all()
    
        
    return render(request,'member.html',locals())

def rfm (request):
    
    #rfmlist test 
    rfm_list = {}
    rfm1 = ''
    one = Customer.objects.get(id = 1)
    his = PurRecord.objects.filter(customer_id = one.id)
    for i in his:
        if i.pur_time =='2019/12':
                if i.buy_total>80:
                    rfm1 = 'best'
                else:
                    rfm1 = 'better'
        else:
            if i.buy_total>80:
                rfm1 = 'not bad'
            else:
                rfm1 = 'bad'
    rfm2 = ''
    two = Customer.objects.get(id = 2)
    his2 = PurRecord.objects.filter(customer_id = two.id)
    for i in his2:
        if i.pur_time =='2019/12':
                if i.buy_total<80:
                    rfm2 = 'better'
                else:
                    rfm2 = 'best'
        else:
            if i.buy_total>80:
                rfm2 = 'not bad'
            else:
                rfm2 = 'bad'
    rfm3 = ''
    three = Customer.objects.get(id = 3)
    his3 = PurRecord.objects.filter(customer_id = three.id)
    for i in his3:
        if i.pur_time =='2019/12':
                if i.buy_total>80:
                    rfm3 = 'best'
                else:
                    rfm3 = 'better'
        else:
            if i.buy_total>80:
                rfm3 = 'not bad'
            else:
                rfm3 = 'bad'
    rfm4 = ''
    four = Customer.objects.get(id = 4)
    his4 = PurRecord.objects.filter(customer_id = four.id)
    for i in his4:
        if i.pur_time =='2019/12':
                if i.buy_total>80:
                    rfm4 = 'best'
                else:
                    rfm4 = 'better'
        else:
            if i.buy_total>80:
                rfm4 = 'not bad'
            else:
                rfm4 = 'bad'
    rfm5 = ''
    five = Customer.objects.get(id = 5)
    his5 = PurRecord.objects.filter(customer_id = five.id)
    for i in his5:
        if i.pur_time =='2019/12':
                if i.buy_total>80:
                    rfm5 = 'best'
                else:
                    rfm5 = 'better'
        else:
            if i.buy_total>80:
                rfm5 = 'not bad'
            else:
                rfm5 = 'bad'
    rfm6 = ''
    six = Customer.objects.get(id = 6)
    his6 = PurRecord.objects.filter(customer_id = six.id)
    for i in his6:
        if i.pur_time =='2019/12':
                if i.buy_total>80:
                    rfm6 = 'best'
                else:
                    rfm6 = 'better'
        else:
            if i.buy_total>80:
                rfm6 = 'not bad'
            else:
                rfm6 = 'bad'
    rfm7 = ''
    seven = Customer.objects.get(id = 7)
    his7 = PurRecord.objects.filter(customer_id = seven.id)
    for i in his7:
        if i.pur_time =='2019/12':
                if i.buy_total>80:
                    rfm7 = 'best'
                else:
                    rfm7 = 'better'
        else:
            if i.buy_total>80:
                rfm7 = 'not bad'
            else:
                rfm7 = 'bad'
    rfm8 = ''
    eight = Customer.objects.get(id = 8)
    his8 = PurRecord.objects.filter(customer_id = eight.id)
    for i in his8:
        if i.pur_time =='2019/12':
                if i.buy_total>80:
                    rfm8 = 'best'
                else:
                    rfm8 = 'better'
        else:
            if i.buy_total>80:
                rfm8 = 'not bad'
            else:
                rfm8 = 'bad'
    rfm9 = ''
    nine = Customer.objects.get(id = 9)
    his9 = PurRecord.objects.filter(customer_id = nine.id)
    for i in his9:
        if i.pur_time =='2019/12':
                if i.buy_total>80:
                    rfm9 = 'best'
                else:
                    rfm9 = 'better'
        else:
            if i.buy_total>80:
                rfm9 = 'not bad'
            else:
                rfm9 = 'bad'
    rfm10 = ''
    ten = Customer.objects.get(id = 10)
    his10 = PurRecord.objects.filter(customer_id = ten.id)
    for i in his10:
        if i.pur_time =='2019/12':
                if i.buy_total<80:
                    rfm10 = 'better'
                else:
                    rfm10 = 'best'
        else:
            if i.buy_total>80:
                rfm10 = 'not bad'
            else:
                rfm10 = 'bad'
    rfm_list.update({one.c_ID:rfm1})
    rfm_list.update({two.c_ID:rfm2})
    rfm_list.update({three.c_ID:rfm3})
    rfm_list.update({four.c_ID:rfm4})
    rfm_list.update({five.c_ID:rfm5})
    rfm_list.update({six.c_ID:rfm6})
    rfm_list.update({seven.c_ID:rfm7})
    rfm_list.update({eight.c_ID:rfm8})
    rfm_list.update({nine.c_ID:rfm9})
    rfm_list.update({ten.c_ID:rfm10})
    #rfm
    
    level1amt = 0
    level2amt = 0
    level3amt = 0
    level4amt = 0
    level5amt = 0
    level6amt = 0
    level7amt = 0
    level8amt = 0
    # level1f = Customer.objects.annotate(num = Count('purrecord'))
    # for i in level1f :
        
    #     for i in level1f:
    #         if i.num >5:
    #             list2.append(i.c_ID)
    level1 = PurRecord.objects.filter(buy_total__gte = 50 , pur_time = '2019/12' ,customer_id__in = [1,2,3,4,5] )
    for j in level1:
        level1amt += j.buy_total
    level2 = PurRecord.objects.filter(buy_total__lte = 50 , pur_time = '2019/12' ,customer_id__in = [1,2,3,4,5] )
    for j in level2:
        level2amt += j.buy_total
    level3 = PurRecord.objects.filter(buy_total__gte = 50 , pur_time = '2019/12' ,customer_id__in =[7,8,9,10] )
    for j in level3:
        level3amt += j.buy_total
    level4 = PurRecord.objects.filter(buy_total__gte = 50 ,customer_id__in = [1,2,3,5] ).exclude(pur_time = '2019/12')
    for j in level4:
        level4amt += j.buy_total 
    level5 = PurRecord.objects.filter(buy_total__lte = 50 ,customer_id__in = [1,2,3,5] ).exclude(pur_time = '2019/12')
    for j in level5:
        level5amt += j.buy_total
    level6 = PurRecord.objects.filter(buy_total__lte = 50 ,customer_id = 4 ).exclude(pur_time = '2019/12')
    for j in level6:
        level6amt += j.buy_total
    level7 = PurRecord.objects.filter(buy_total__lte = 50 , pur_time = '2019/12' ,customer_id__in = [7,8,9,10] )
    for j in level7:
        level7amt += j.buy_total
    level8 = PurRecord.objects.filter(buy_total__lte = 50 ,customer_id = 4 ).exclude(pur_time = '2019/12')
    for j in level8:
        level8amt += j.buy_total
    #rfm 圖表結束

    return render(request,'rfm.html',locals())

def data(request):
    drinks = Item.objects.all()
    drinklist = list(drinks)
    drinklist1 = drinklist[0]
    
    drinklist2 = drinklist[1]
    drinklist3 = drinklist[2]
    drinklist4 = drinklist[3]
    drinklist5 = drinklist[4]
    drink1amt = drinklist1.item_price*drinklist1.item_sales
    drink2amt= drinklist2.item_price*drinklist2.item_sales
    drink3amt = drinklist3.item_price*drinklist3.item_sales
    drink4amt = drinklist4.item_price*drinklist4.item_sales
    drink5amt = drinklist5.item_price*drinklist5.item_sales
    
    
    
    date = PurRecord.objects.all()
    datelist = []
    date = list(date)
    for i in range(len(date)):
        datelist.append(date[i].pur_time)
    #print(datelist)
#留存率
    root_list = []
    root = PurRecord.objects.filter(pur_time = '2019/10')
    for i in root:
        root_list.append(i.customer_id)
        root_list = list(set(root_list))
    node1_list = []
    node1 = PurRecord.objects.filter(pur_time = '2019/11')
    for i in node1:
        if i.customer_id in root_list:
            node1_list.append(i.customer_id)
    node2_list = []
    node2 = PurRecord.objects.filter(pur_time = '2019/12')
    for i in node2:
        if i.customer_id in node1_list:
            node2_list.append(i.customer_id) 
    root_len = len(root_list)
    node1_len = len(node1_list)
    node2_len = len(node2_list)
    firstrate = node1_len/root_len
    secondrate = node2_len/node1_len

#10月
    sale101amt = 0
    sale101 = PurRecord.objects.filter(pur_time = '2019/10',item_num= 1)
    for i in sale101:
        sale101amt += i.buy_total
    sale102amt = 0
    sale102 = PurRecord.objects.filter(pur_time = '2019/10',item_num= 2)
    for i in sale102:
        sale102amt += i.buy_total
    sale103amt = 0
    sale103 = PurRecord.objects.filter(pur_time = '2019/10',item_num= 3)
    for i in sale103:
        sale103amt += i.buy_total
    sale104amt = 0
    sale104 = PurRecord.objects.filter(pur_time = '2019/10',item_num= 4)
    for i in sale104:
        sale104amt += i.buy_total
    sale105amt = 0
    sale105 = PurRecord.objects.filter(pur_time = '2019/10',item_num= 5)
    for i in sale105:
        sale105amt += i.buy_total
#11月
    sale111amt = 0
    sale111 = PurRecord.objects.filter(pur_time = '2019/11',item_num= 1)
    for i in sale111:
        sale111amt += i.buy_total
    sale112amt = 0
    sale112 = PurRecord.objects.filter(pur_time = '2019/11',item_num= 2)
    for i in sale112:
        sale112amt += i.buy_total
    sale113amt = 0
    sale113 = PurRecord.objects.filter(pur_time = '2019/11',item_num= 3)
    for i in sale113:
        sale113amt += i.buy_total
    sale114amt = 0
    sale114 = PurRecord.objects.filter(pur_time = '2019/11',item_num= 4)
    for i in sale114:
        sale114amt += i.buy_total
    sale115amt = 0
    sale115 = PurRecord.objects.filter(pur_time = '2019/11',item_num= 5)
    for i in sale115:
        sale115amt += i.buy_total
#12月
    sale121amt = 0
    sale121 = PurRecord.objects.filter(pur_time = '2019/12',item_num= 1)
    for i in sale121:
        sale121amt += i.buy_total
    sale122amt = 0
    sale122 = PurRecord.objects.filter(pur_time = '2019/12',item_num= 2)
    for i in sale122:
        sale122amt += i.buy_total
    sale123amt = 0
    sale123 = PurRecord.objects.filter(pur_time = '2019/12',item_num= 3)
    for i in sale123:
        sale123amt += i.buy_total
    sale124amt = 0
    sale124 = PurRecord.objects.filter(pur_time = '2019/12',item_num= 4)
    for i in sale124:
        sale124amt += i.buy_total
    sale125amt = 0
    sale125 = PurRecord.objects.filter(pur_time = '2019/12',item_num= 5)
    for i in sale125:
        sale125amt += i.buy_total
    
    return render(request,'data.html',locals())

# def inventory(request):
#     return render(request,'inventory.html')

# def material(request):
#     return render(request,'material.html')

def index(request):
    date = PurRecord.objects.all()
    datelist = []
    for i in date:
        datelist.append(i.pur_time)
    name = Customer.objects.get(c_name = 'dave')
    num1 = Customer.objects.filter(c_sex = 1)
    j = len(num1)
    month = PurRecord.objects.get(trade_num = 20190907001)
    
    #rfm
    
    level1amt = 0
    
    # level1f = Customer.objects.annotate(num = Count('purrecord'))
    # for i in level1f :
        
    #     for i in level1f:
    #         if i.num >5:
    #             list2.append(i.c_ID)
    level1 = PurRecord.objects.filter(buy_total__gte = 50 , pur_time = '2019/12')
    
    for j in level1:
        level1amt += j.buy_total

    
   
    return render(request,'index.html',locals())
# def tables(request):
#     return render(request,'tables.html',locals())
