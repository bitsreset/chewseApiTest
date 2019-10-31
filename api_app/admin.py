from django.contrib import admin
from .models import Item,Order,PortionDetails
# Register your models here.
#joy
#joy@email.com
#password1234

class ItemAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('id', 'name',)

class OrderAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('id', 'order_dict','portions')

class PortionDetailsAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('orderID', 'itemID','item','ratio','allocated_portions',)


admin.site.register(Item,ItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(PortionDetails,PortionDetailsAdmin)