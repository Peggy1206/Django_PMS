from django.db import models
import datetime
# Create your models here.

class Raw_Material(models.Model):
    m_number = models.IntegerField(primary_key=True) #編號
    m_name = models.CharField(max_length=10) #原料名字
    m_left_amount = models.IntegerField() #剩餘量 left_amount
    m_safe_inventory = models.IntegerField() #安全庫存 safe_inventory

    def __str__(self):
        return '原料編號:{0} 原料名稱:{1}'.format(self.m_number, self.m_name)

class product(models.Model):
    pd_id = models.IntegerField(primary_key=True) #編號
    pd_name = models.CharField(max_length=20) #品名
    pd_price = models.IntegerField() #單價
    blackTea = models.IntegerField(default=0) #紅茶
    milk = models.IntegerField(default=0) #牛奶
    pearl = models.IntegerField(default=0) #珍珠
    taro = models.IntegerField(default=0) #小芋圓
    honey = models.IntegerField(default=0) #蜂蜜
    
class DailyRecord(models.Model):                                            #記錄每天的量
    sell_date = models.DateField(('Date'), default=datetime.date.today)
    sell_pd1 = models.IntegerField(default=0)     #濃厚奶茶今天的銷量
    sell_pd2 = models.IntegerField(default=0)     #濃厚小芋圓今天的銷量
    sell_pd3 = models.IntegerField(default=0)   #濃厚珍珠奶茶今天的銷量
    sell_pd4 = models.IntegerField(default=0)   #特濃蜂蜜牛奶今天的銷量
    # choices = (
    #     ('存貨足夠：','不用訂貨'),
    #     ('存貨不足','記得訂貨')
    # )
    sell_pd5 = models.IntegerField(default=0)   #蜂蜜珍珠鮮奶今天的銷量
    
    # p_name = models.CharField(max_length = 10)
    # p_price = models.IntegerField()
    # blacktea = models.IntegerField(default=0)
    # milk = models.IntegerField(default=0)
    # pearl = models.IntegerField(default=0)
    # taro = models.IntegerField(default=0)
    # honey = models.IntegerField(default=0)
    
    def __datetime__(self):
           return self.sell_date                #從後台選日期

class addMaterial(models.Model):               #從後台新增進貨量
    add_date = models.DateField(('Date'), default=datetime.date.today)
    add_blacktea = models.IntegerField(default=0)
    add_milk = models.IntegerField(default=0)
    add_pearl = models.IntegerField(default=0)
    add_taro = models.IntegerField(default=0)
    add_honey = models.IntegerField(default=0)
    

# class LeftMatirial(models.Model): 
#     left_blacktea = models.DecimalField(max_digits=10, decimal_places=2,default =0)                                           #記錄每天的量
#     left_milk = models.DecimalField(max_digits=10, decimal_places=2,default = 0)     #濃厚奶茶剩下的量
#     left_peral = models.DecimalField(max_digits=10, decimal_places=2,default = 0)     #濃厚小芋圓剩下的量
#     left_toro = models.DecimalField(max_digits=10, decimal_places=2,default = 0)   #濃厚珍珠奶茶剩下的量