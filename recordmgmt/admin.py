from django.contrib import admin
from .forms import StockCreateForm


from .models import *


class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'created_by']
   form = StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name', 'created_by']

admin.site.register(record, StockCreateAdmin)
admin.site.register(Category)