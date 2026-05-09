from django.contrib import admin
from .models import Order, OrderItem


class OrderitemInline(admin.TabularInline):
    model = OrderItem
    ''' оптимизирует форму, используя виджет с необработанным
      идентификатором (raw_id) для поля product вместо выпадающего списка,
        что повышает производительность при работе с большим количеством
          продуктов, избегая загрузки всех параметров в память '''
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']