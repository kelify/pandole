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


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    def has_add_permission(self, request):
        if len(CompanyInfo.objects.all())>=1:
            return  False
        else :
            return True




class MenuAdmin(admin.ModelAdmin):
    list_display = ('label',)
    fields= ('style','label','menuweight',)

    def save_model(self, request, obj, form, change):
        if obj.style == '1' :
            obj.menurl  = 'styleone'
            style = Styleone(label=obj.label)
            style.save()
            obj.styleid = style.pk
        else:
            obj.menurl  = 'styletwo'
            style = Styletwo(label=obj.label)
            style.save()
            obj.styleid = style.pk
        obj.user = request.user
        obj.save()

    def delete_model(self, request, obj):
        """
        Given a model instance delete it from the database.
        """
        if obj.style == '1' :
            Styleone.objects.get(id=obj.styleid).delete()
            print(obj.styleid)
        else:
            Styletwo.objects.get(id=obj.styleid).delete()
        obj.delete()

class ImageRunAdmin(admin.ModelAdmin):
    list_display = ('Title',)
    search_fields = ('Title',)

class FooterContentAdmin(admin.ModelAdmin):
    list_display = ('Title',)
    search_fields = ('Title',)

admin.site.register(ImageRun,ImageRunAdmin)
admin.site.register(FooterContent,FooterContentAdmin)

admin.site.register(New,NewAdmin)
#admin.site.register(Styleone,StyleoneAdmin)
admin.site.register(CompanyInfo,CompanyInfoAdmin)
#admin.site.register(Styletwo,StyletwoAdmin)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Category,CategoryAdmin)

