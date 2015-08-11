from django.contrib import admin
from sidebarStyle.models import Sidebar,PageOfSidebar
class PageOfSidebarInline(admin.StackedInline):
    model = PageOfSidebar
    extra = 1

class SidebarAdmin(admin.ModelAdmin):
    inlines = [PageOfSidebarInline]
    list_display = [ 'label',]
    readonly_fields = ['label']

    def has_add_permission(self, request):
        return  False
admin.site.register(Sidebar,SidebarAdmin)