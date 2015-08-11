from django.template.response import TemplateResponse
from django.http  import HttpResponse
from cms.models import *


# Create your views here.
from django.shortcuts import render
from django.http  import HttpResponse
from django.template import loader ,Context
from cms.models import *
import operator

 # Create your views here.
NEWS_OF_A_PAGE = 20



index(request):
    try:
        companyinfo = CompanyInfo.objects.all()[0]
        FC = FooterContent.objects.all()
        Img = ImageRun.objects.all()
    except:
        companyinfo = []
    menulist = Menu.objects.all().order_by('menuweight')
    return TemplateResponse(request,'index.html',{
        'menulist':menulist,
        'FCL1':FC[0],
        'FCL2':FC[1],
        'FCL3':FC[2],
        'Img1':Img[0],
        'Img2':Img[1],
        'Img3':Img[2],
        'companyinfo':companyinfo,
    })
 
getnewslist(request):
    try:
        if 'load' in  request.GET.keys():
            load = request.GET.key('load')
        else:
            load = 1
    except:
        load = 1
    page_count = load*NEWS_OF_A_PAGE
    try:
        newslist = New.objects.all()[0:page_count]
    except:
        newslist = New.objects.all()
    categorylist = Category.objects.all()
    try:
       companyinfo = CompanyInfo.objects.all()[0]
    except:
        companyinfo = []

    menulist = Menu.objects.all().order_by('menuweight')
    return TemplateResponse(request,'news.html',{
        'newslist':newslist,
        'menulist':menulist,
        'categorylist':categorylist,
        'comapnyinfo':companyinfo,
    })

def getnewsofcategory(requset,*args,**kwargs):
    try:
        if 'category' in requset.GET.keys():
            category = requset.GET.get('category')
            print(requset.GET.keys())
            print(category)
        else:
            return HttpResponse("error")

        if 'load' in requset.GET.keys():
            load = requset.GET.get('load')
        else:
            load = 1
    except:
        load = 1

    print("start")
    page_count = load*NEWS_OF_A_PAGE
    try:
        newslist = New.objects.filter(category_id=category)[0:page_count]
    except:
        newslist = New.objects.filter(category_id=category)
    categorylist = Category.objects.all()
    print(newslist)
    try:
       companyinfo = CompanyInfo.objects.all()[0]
    except:
        companyinfo = []

    menulist = Menu.objects.all().order_by('menuweight')
    return TemplateResponse(requset,'news.html',{
        'newslist':newslist,
        'categorylist':categorylist,
        'menulist':menulist,
        'comapnyinfo':companyinfo,
    })


def getnewsdetial(request):
    try:
        id = request.GET.get('id')
    except:
        return HttpResponse("error")
    menulist = Menu.objects.all().order_by('menuweight')
    news = New.objects.get(id=id)
    try:
       companyinfo = CompanyInfo.objects.all()[0]
    except:
        companyinfo = []

    categorylist = Category.objects.all()
    return TemplateResponse(request,'newsdetial.html',{
        'news':news,
        'menulist':memulist,
        'comapnyinfo':companyinfo,
        'categorylist':categorylist,
    })


<<<<<<< HEAD
def styleone(request):
    try:
        menu_id = request.GET.get('menu_id')
    except:
        return HttpResponse('error')

    pageofmenulist = PageOfStyleone.objects.filter(menu_id=menu_id)
    menulist = Menu.objects.all().order_by('menuweight')
    try:
        head = Head.objects.all()[0]
        footer = Footer.objects.all()[0]
    except:
        head = []
        footer = []
    return TemplateResponse(request,'pageofmenu.html',{
        'pageofmenulist':pageofmenulist,
        'menulist':menulist,
        'head':head,
        'footer':footer,
    })


def styletwo(request):
    try:
        menu_id = request.GET.get('menu_id')
    except:
        return HttpResponse('error')

    pageofmenulist = PageOfStyletwo.objects.get(menu_id=menu_id)
    menulist = Menu.objects.all().order_by('menuweight')
    try:
        head = Head.objects.all()[0]
        footer = Footer.objects.all()[0]
    except:
        head = []
        footer = []
    return TemplateResponse(request,'styletwo.html',{
        'pageofmenulist':pageofmenulist,
        'menulist':menulist,
        'head':head,
        'footer':footer,
    })

=======
>>>>>>> 15b7118d1f83265826853fedc8ccc754d6506682



