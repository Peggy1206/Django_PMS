from django.db import models
from _datetime import date

# Create your models here.
class Customer(models.Model):

    c_name = models.CharField(max_length=11)   #顧客名:最大長度為11
    c_ID = models.IntegerField()    #卡號:是一串整數，最大長度為11 (2014/12/25辦卡的就打: 20141225001)
    c_sex = models.IntegerField()                 #性別:1:male  2:female
    c_point = models.IntegerField(default=0) 
    c_birth = models.DateField(default=date.today)     #累計點數:預設為0
    def __integer__(self):
        return self.c_ID


class Item(models.Model):                        #這裡記載，以及這個月的銷量
    item_num = models.IntegerField(primary_key=True)             #品項編號:五杯品項有不同編號(1~5)
    item_name = models.CharField(max_length=20)  #品項名稱
    item_price = models.DecimalField(max_digits=3,decimal_places=0)  #各品項價錢
    item_sales = models.IntegerField(default=0)        #這個月的銷量:預設為0

# class PurRecord(models.Model):
#     trade_num = models.IntegerField()           #交易編號:最大長度為11(2019/12/25買的就打:20191225001)
#     c_ID = models.ForeignKey(Customer.c_ID,on_delete=models.CASCADE)     #顧客卡號(判斷這筆紀錄是誰的,若同個人買了不同飲料，就算兩筆不同紀錄)
#                                                                          #on_delete = models.CASCADE 表示一對一關係，要是有 foreign key的時候記得要加
#     item_num = models.ForeignKey(Item.item_num,on_delete=models.CASCADE) #買了甚麼
#     buy_amount = models.IntegerField(default=0)   #買了幾杯
#     buy_total = models.IntegerField()             #買的總價格  這裡之後要讓上面兩項相乘
#     pur_time = models.DateTimeField(auto_now_add=True)  #新增資料時會?你自動加上建立時間

class PurRecord(models.Model):
    trade_num = models.IntegerField(primary_key=True)           #交易編號:最大長度為11(2019/12/25買的就打:20191225001)
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL,blank = True,null=True)     #顧客卡號(判斷這筆紀錄是誰的,若同個人買了不同飲料，就算兩筆不同紀錄)
                                                                         #on_delete = models.CASCADE 表示一對一關係，要是有 foreign key的時候記得要加
   
    item_num = models.ForeignKey(Item, on_delete = models.CASCADE) #買了甚麼
    buy_amount = models.IntegerField(default=0)   #買了幾杯
    buy_total = models.IntegerField()              #買的總價格  這裡之後要讓上面兩項相乘
    pur_time = models.CharField(max_length=7)    #新增資料時會?