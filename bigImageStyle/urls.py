from django.conf.urls import include, url
from bigImageStyle.views import bigimage
urlpatterns = [
    url(r'bigimage',bigimage),
]
