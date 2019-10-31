from django.db import models
from django.utils import timezone


class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_dict = models.CharField(max_length=150)
    portions = models.PositiveIntegerField(null=True, default=None)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.order_dict

class PortionDetails(models.Model):
    # orderID =models.ForeignKey(Order,on_delete=models.CASCADE,to_field="id",name="orderID",related_name='PortionDetails_orderID')
    orderID = models.PositiveIntegerField(null=True, default=None)
    # itemID = models.ForeignKey(Item,to_field="id",name="itemID",on_delete=models.CASCADE,related_name='PortionDetails_itemid')
    itemID = models.PositiveIntegerField(null=True, default=None)
    # item = models.ForeignKey(Item,to_field='name',on_delete=models.CASCADE,related_name='PortionDetails_itemName')
    #item_name = models.CharField(max_length=50)
    item = models.ForeignKey(Item,to_field="name",on_delete=models.CASCADE,related_name='PortionDetails_itemName',default=None)
    ratio = models.PositiveIntegerField(null=True, default=None)
    allocated_portions = models.PositiveIntegerField(null=True, default=None)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{0},{1},{2}".format(self.itemID,self.item,self.allocated_portions)



