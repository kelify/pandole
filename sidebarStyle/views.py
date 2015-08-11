from django.template.response import TemplateResponse
from django.http  import HttpResponse
from cms.models import *
from django.shortcuts import render
from django.http  import HttpResponse
from django.template import loader ,Context
from cms.models import *
from sidebarStyle import *
import operator

NEWS_OF_A_PAGE = 20



def sidebar(request):
    try:
        menu_id = request.GET.get('menu_id')
    except:
        return HttpResponse('error')

    pageofSoderbarlist = PageOfSidebar.objects.filter(menu_id=menu_id)
    menulist = Menu.objects.all().order_by('menuweight')
    try:
       companyinfo = CompanyInfo.objects.all()[0]
    except:
        companyinfo = []
    return TemplateResponse(request,'pageofmenu.html',{
        'pageofmenulist':pageofSoderbarlist,
        'menulist':menulist,
        'companyinfo':companyinfo,
    })





