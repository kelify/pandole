from django.contrib import admin
from bigImageStyle.models import  *

class PageOfBigImageStyleInline(admin.StackedInline):
    model = PageOfBigImageStyle
    extra = 1
    max_num = 1

class BigImageStyleAdmin(admin.ModelAdmin):
    inlines = (PageOfBigImageStyleInline,)
    list_display = ('label',)
    def has_add_permission(self, request):
        return  True

admin.site.register(BigImageStyle,BigImageStyleAdmin)