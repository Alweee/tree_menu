from django.contrib import admin

from tree_menu.models import Product


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',
                    'description', 'date_created', 'tags')
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Product, MenuAdmin)
