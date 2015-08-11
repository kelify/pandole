#coding:utf-8
from django.db import models

from markdown import markdown

class Category(models.Model):
    label = models.CharField(max_length = 20)

    class Meat:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.label

class Head (models.Model):
    company_name = models.CharField(max_length = 30)
    company_logo = models.FileField(upload_to = "static/file")

class Footer(models.Model):
    company_name = models.CharField(max_length = 30 )
    company_date_range = models.CharField(max_length = 20)
    company_signature = models.CharField(max_length = 20 )

class  New (models.Model):
    title = models.CharField(max_length = 100)
    category = models.ForeignKey(Category)
    html_content = models.TextField(blank=True)
    content = models.TextField()
    createtime = models.DateTimeField()

    def save(self):
        self.html_content = markdown(self.content)

        super(New,self).save()

    class Mete:
        ordering = ['createtime']
    def __str__(self):
        return self.title

class Menu(models.Model):
    STYLE = (
        ('1', '风格一'),
        ('2', '风格二'),
    )
    style = models.CharField(max_length = 1 ,choices = STYLE)
    label = models.CharField(max_length = 20)
    menurl = models.CharField(max_length = 50)
    menuweight = models.IntegerField()
    styleid = models.BigIntegerField()

class Styleone (models.Model):
    label = models.CharField(max_length = 20 )

class  PageOfStyleone(models.Model):
    menu = models.ForeignKey(Styleone)
    label = models.CharField(max_length = 20)
    content = models.TextField()

class Styletwo (models.Model):
    label = models.CharField(max_length = 20 )

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

