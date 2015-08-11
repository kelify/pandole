from django.conf.urls import include, url
from sidebarStyle.views import sidebar
urlpatterns = [
    url(r'sidebar',sidebar),
]
