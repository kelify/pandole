1. 将 "bigImageStyle" 加入 settings.py 文件中:

    INSTALLED_APPS = (
        ...
        'polls',
    )


2. 将 bigImageStyle URLconf 写入项目的 urls.py 文件中:

    url(r'', include('bigImageStyle.urls')),


3.bigImageStyle AppInfo中的变量写入项目的base_settings 文件中：

    from bigImageStyle import AppInfo as xxx
    STYLE = (
        ...
        xxx.STYLE_CHOICE,
    )

    STYLE_LIST = {
        ...
        xxx.STYLE_NAME:AppInfo.STYLE_OBJECT,
    }

    STYLE_URL_LIST ={
        ...
        xxx.STYLE_NAME:AppInfo.STYLE_URL,
    }


4.运行 `python manage.py migrate` 指令创建 bigImageStyle models.
