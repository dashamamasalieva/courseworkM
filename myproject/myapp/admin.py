from django.contrib import admin
from .models import Goog, Reviews, Orders, Stat,  TypeOfService

admin.site.register(Goog)
admin.site.register(Reviews)
admin.site.register(TypeOfService)
@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'stat', 'prod', 'description', 'owner', 'service')
    list_display_links = ('id', 'created', 'stat', 'prod', 'description', 'owner', 'service')

