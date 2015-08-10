#coding:utf-8
from django.contrib import admin
from django.db import models
from cms.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_dispaly = ('label',)

class PageOfMenuMenuAdmin(admin.ModelAdmin):
    list_display = ('label',)


class NewAdmin(admin.ModelAdmin):
    list_display = ('title','createtime',)
    search_fields = ('title',)
    list_filter = ('title',)

class FooterAdmin(admin.ModelAdmin):
    list_display = ('company_name',)

class HeadAdmin(admin.ModelAdmin):
    list_display = ('company_name',)

class PageOfMenuMenuAdmin(admin.ModelAdmin):
    list_display = ['label']


class NewAdmin(admin.ModelAdmin):
    list_display = ['title','createtime']

class FooterAdmin(admin.ModelAdmin):
    list_display = ['company_name']

class HeadAdmin(admin.ModelAdmin):
    list_display = ['company_name']

class PageOfStyleoneInline(admin.StackedInline):
    model = PageOfStyleone
    extra = 1

class StyleoneAdmin(admin.ModelAdmin):
    inlines = [PageOfStyleoneInline]
    list_display = [ 'label',]
    readonly_fields = ['menu']

class PageOfStyletwoInline(admin.StackedInline):
    model = PageOfStyletwo
    extra = 1
    max_num = 1
class StyletwoAdmin(admin.ModelAdmin):
    inlines = (PageOfStyletwoInline,)
    list_display = ('label',)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('label',)
    fields= ('style','label','menuweight',)
    inlines = [PageOfStyletwoInline]

class MenuAdmin(admin.ModelAdmin):
    list_display = ['label']
    fields= ('style','label','menuweight')
    #readonly_fields = ['style']
    actions = []
   
admin.site.register(New,NewAdmin)
admin.site.register(Footer,FooterAdmin)
admin.site.register(Head,HeadAdmin)
admin.site.register(Styleone,StyleoneAdmin)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Styletwo,StyletwoAdmin)
admin.site.register(Category,CategoryAdmin)

