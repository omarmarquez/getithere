from django.contrib import admin
from .models import *
# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name',)

    class Meta:
        abstract = True


class LocationAdmin(BaseAdmin):
    pass

admin.site.register(Location, LocationAdmin)

class OwnerAdmin(BaseAdmin):
    pass

admin.site.register(Owner, OwnerAdmin)

class ItemAdmin(BaseAdmin):
    pass

admin.site.register(Item, ItemAdmin)

class CustomerAdmin(BaseAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)

class BookingAdmin(BaseAdmin):
    list_display = ('get_owner','get_item','get_customer','start_dt','end_dt')

    def get_owner(self, obj):
        return obj.item.owner.name
    get_owner.short_description = 'Owner'
    get_owner.admin_order_field = 'owner__name'

    def get_item(self, obj):
        return obj.item.name
    get_item.short_description = 'Item'
    get_item.admin_order_field = 'item__name'

    def get_customer(self, obj):
        return obj.customer.name
    get_customer.short_description = 'Customer'
    get_customer.admin_order_field = 'customer__name'

admin.site.register(Booking, BookingAdmin)

class PictureAdmin(BaseAdmin):
    pass

admin.site.register(Picture, PictureAdmin)