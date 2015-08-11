from django.db import models

# Create your models here.

class BigImageStyle (models.Model):
    label = models.CharField(verbose_name="菜单名称",max_length = 20 )
    class Meta:
        verbose_name = "大图风格"
        verbose_name_plural = "大图风格"

class  PageOfBigImageStyle(models.Model):
    menu = models.ForeignKey(BigImageStyle,verbose_name="大图风格内容编辑")
    content = models.TextField(verbose_name="内容")
    maximage = models.FileField(verbose_name="图片",upload_to = "bigImageStyle/static/file")