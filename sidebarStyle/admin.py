from django.contrib import admin
from sidebarStyle.models import Sidebar,PageOfSidebar
class PageOfSidebarInline(admin.StackedInline):
    model = PageOfSidebar
    extra = 1

class SidebarAdmin(admin.ModelAdmin):
    inlines = [PageOfSidebarInline]
    list_display = [ 'label',]
    readonly_fields = ['label']

admin.site.register(Sidebar,SidebarAdmin)