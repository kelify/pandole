from django.template.response import TemplateResponse
from django.http  import HttpResponse
from cms.models import *
from django.shortcuts import render
from django.http  import HttpResponse
from django.template import loader ,Context
from cms.models import *
from bigImageStyle.models import  PageOfBigImageStyle
NEWS_OF_A_PAGE = 20



def bigimage(request):
    try:
        menu_id = request.GET.get('menu_id')
    except:
        return HttpResponse('error')

    pageofmenulist = PageOfBigImageStyle.objects.get(menu_id=menu_id)
    menulist = Menu.objects.all().order_by('menuweight')
    try:
       companyinfo = CompanyInfo.objects.all()[0]
    except:
        companyinfo = []

    print(pageofmenulist)
    return TemplateResponse(request,'styletwo.html',{
        'pageofmenulist':pageofmenulist,
        'menulist':menulist,
        'companyinfo':companyinfo,
    })






