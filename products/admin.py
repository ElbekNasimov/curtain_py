from django.contrib import admin
from .models import Category, Location, MeasureType, Product, ProductImage, Cost, OutlayType, Outlay
# Register your models here.


class ProductImageInliner(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'length', 'storage', 'description', 'author']
    inlines = (ProductImageInliner,)
    search_fields = ('title', 'category',)


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(MeasureType)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Cost)
admin.site.register(OutlayType)
admin.site.register(Outlay)
