from django.contrib import admin
from .models import Size, Color, GeneralCategory, Category, Campaign, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ['image_tag']
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_filter = ['categories']

admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(GeneralCategory)
admin.site.register(Category)
admin.site.register(Campaign)
admin.site.register(ProductImage)



