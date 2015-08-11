from django.db import models
#from cms.models import Menu

class Sidebar (models.Model):
    #menu = models.OneToOneField(Menu,verbose_name="菜单名称",)
    label = models.CharField(blank= False,verbose_name="菜单名称" ,max_length = 20 )
    class Meta:
        verbose_name = "侧边栏风格"
        verbose_name_plural = "侧边栏风格"

class  PageOfSidebar(models.Model):
    menu = models.ForeignKey(Sidebar,verbose_name="菜单风格")
    label = models.CharField(verbose_name = "小标题",max_length = 20)
    content = models.TextField(verbose_name = "内容")