from django.contrib import admin

from . import models as _m

# Register your models here.


class ImageInline(admin.StackedInline):
    model = _m.Images
    fields = ('id', 'Url', 'is_deleted')
    can_delete = False
    show_change_link = True


@admin.register(_m.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_deleted', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'is_deleted')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    inlines = (ImageInline, )


@admin.register(_m.Variants)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_deleted', 'created_at', 'updated_at')
    list_display_links = ('id', 'name', 'is_deleted')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    inlines = (ImageInline, )


@admin.register(_m.Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_deleted', 'product', 'variant', 'Url', 'created_at', 'updated_at')
    list_display_links = ('id', 'is_deleted', 'product', 'variant')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
