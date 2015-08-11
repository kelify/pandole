#coding:utf-8
from django.db import models
from companycms.base_settings import  STYLE,STYLE_LIST,STYLE_URL_LIST
from sidebarStyle.models import *
from markdown import markdown
class Category(models.Model):
    label = models.CharField(max_length = 20)
    class Meta:
        verbose_name = "ÐÎ·Öà        verbose_name_plural = "ÐÎ·Öà    def __str__(self):
        return self.label
class CompanyInfo (models.Model):
    company_name = models.CharField(verbose_name="ÆҵÃ³Æ,max_length = 30)
    company_logo = models.FileField(verbose_name="Æҵlogo",upload_to = "static/file")
    company_date_range = models.CharField(verbose_name="Æҵ´´bÄ·Ý,max_length = 10)
    company_signature = models.CharField(verbose_name="ÆҵǩÃ",blank= True,max_length = 20 )
    class Meta:
        verbose_name = "ÆҵÐϢ"
        verbose_name_plural = "ÆҵÐϢ"
class  New (models.Model):
    title = models.CharField(max_length = 100)
    category = models.ForeignKey(Category)
    html_content = models.TextField(blank=True)
    content = models.TextField()
    createtime = models.DateTimeField()
    class Meta:
        verbose_name = "ÐÎ"
        verbose_name_plural = "ÐÎ"
    def save(self):
        self.html_content = markdown(self.content)
        super(New,self).save()
    class Mete:
        ordering = ['createtime']
    def __str__(self):
        return self.title
class Menu(models.Model):
    style = models.CharField(verbose_name="²˵¥·ç",max_length = 10 ,choices = STYLE)
    label = models.CharField(verbose_name="²˵¥Ã³Æ,max_length = 20)
    menurl = models.CharField(max_length = 50,blank = True,null = True)
    menuweight = models.IntegerField(verbose_name="²˵¥ÅÐ",)
    styleid = models.BigIntegerField(blank = True,null = True)
    class Meta:
        verbose_name = "²˵¥"
        verbose_name_plural = "²˵¥"
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
    menu = models.OneToOneField(Menu,verbose_name="²˵¥Ã³Æ,)
    label = models.CharField(verbose_name="²˵¥Ã³Æ ,max_length = 20 )
    class Meta:
        verbose_name = "²˵¥·çһ"
        verbose_name_plural = "²˵¥·çһ"
class  PageOfStyleone(models.Model):
    menu = models.ForeignKey(Styleone,verbose_name="²˵¥·ç")
    label = models.CharField(verbose_name = "С±ê",max_length = 20)
    content = models.TextField(verbose_name = "ÄÈ")
class Styletwo (models.Model):
    menu = models.OneToOneField(Menu)
    label = models.CharField(max_length = 20 )
    class Meta:
        verbose_name = "²˵¥·ç¶þ"
        verbose_name_plural = "²˵¥·ç¶þ"
class  PageOfStyletwo(models.Model):
    menu = models.ForeignKey(Styletwo)
    content = models.TextField()
    maximage = models.FileField(upload_to = "static/file")


class ImageRun(models.Model):
    Title = models.CharField(max_length=20)
    Picture = models.ImageField(upload_to="static/file")
    Url = models.URLField()

    def __str__(self):
        return self.Title

class FooterContent(models.Model):
    Title = models.CharField(max_length=20)
    Article = models.TextField()

