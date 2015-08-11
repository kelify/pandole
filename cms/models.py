#coding:utf-8
from django.db import models
from companycms.base_settings import  STYLE,STYLE_LIST,STYLE_URL_LIST
from sidebarStyle.models import *
from markdown import markdown

class Category(models.Model):
    label = models.CharField(max_length = 20)

    class Meta:
        verbose_name = "新闻分类"
        verbose_name_plural = "新闻分类"

    def __str__(self):
        return self.label

class Head (models.Model):
    company_name = models.CharField(max_length = 30)
    company_logo = models.FileField(upload_to = "static/file")

class Footer(models.Model):
    company_name = models.CharField(max_length = 30 )
    company_date_range = models.CharField(max_length = 10)
    company_signature = models.CharField(max_length = 20 )

class  New (models.Model):
    title = models.CharField(max_length = 100)
    category = models.ForeignKey(Category)
    html_content = models.TextField(blank=True)
    content = models.TextField()
    createtime = models.DateTimeField()
    class Meta:
        verbose_name = "新闻"
        verbose_name_plural = "新闻"
    def save(self):
        self.html_content = markdown(self.content)

        super(New,self).save()

    class Mete:
        ordering = ['createtime']
    def __str__(self):
        return self.title

class Menu(models.Model):
    style = models.CharField(verbose_name="菜单风格",max_length = 10 ,choices = STYLE)
    label = models.CharField(verbose_name="菜单名称",max_length = 20)
    menurl = models.CharField(max_length = 50,blank = True,null = True)
    menuweight = models.IntegerField(verbose_name="菜单排序",)
    styleid = models.BigIntegerField(blank = True,null = True)

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = "菜单"

    def save(self):
        if self.pk == None:
            self.menurl = STYLE_URL_LIST[self.style]
            super(Menu,self).save()
            style = STYLE_LIST[self.style](label=self.label)
            style.save()
            menu = Menu.objects.get(id = self.pk)
            menu.styleid = style.pk
            super(Menu,menu).save()
        else:
            menu = Menu.objects.get(id = self.pk)
            menu.label = self.label
            menu.menuweight = self.menuweight
            super(Menu,menu).save()

    def __str__(self):
        return self.label

class Styleone (models.Model):
    menu = models.OneToOneField(Menu,verbose_name="菜单名称",)
    label = models.CharField(verbose_name="菜单名称" ,max_length = 20 )
    class Meta:
        verbose_name = "菜单风格一"
        verbose_name_plural = "菜单风格一"

class  PageOfStyleone(models.Model):
    menu = models.ForeignKey(Styleone,verbose_name="菜单风格")
    label = models.CharField(verbose_name = "小标题",max_length = 20)
    content = models.TextField(verbose_name = "内容")

class Styletwo (models.Model):
    menu = models.OneToOneField(Menu)
    label = models.CharField(max_length = 20 )
    class Meta:
        verbose_name = "菜单风格二"
        verbose_name_plural = "菜单风格二"

class  PageOfStyletwo(models.Model):
    menu = models.ForeignKey(Styletwo)
    content = models.TextField()
    maximage = models.FileField(upload_to = "static/file")
