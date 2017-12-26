"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))


"""
from django.conf.urls import include, url
from django.contrib import admin
from DemoProject.views import hello_world
from DemoProject.views import UsingStaticSource
from DemoProject.views import Http_From_Get
from DemoProject.views import Http_From_Post
from DemoProject.views import For_Cycle
from DemoProject.views import Who_am_I
from DemoProject.views import import_vegetable
from DemoProject.views import search_price_by
from DemoProject.views import get_vegetable_by_id
from DemoProject.views import follow_vegetable
from DemoProject.views import report_vegetable_price
from DemoProject.views import get_reported_price
from DemoProject.views import abort_report
urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^Demo/$', hello_world),
    url(r'^Demo/static_url/$', UsingStaticSource),
    url(r'^Demo/Cycle/$', For_Cycle),
    url(r'^Demo/Get/(?P<input1>\S*)/(?P<input2>\S*)/$', Http_From_Get),#http://....../Demo/Get/HELLO/WORLD/
    url(r'^Demo/Post/$', Http_From_Post),
    url(r'^Demo/WhoamI/$', Who_am_I),
    url(r'^Demo/import_vegetable/$', import_vegetable),
    url(r'^Demo/search/$', search_price_by),
    url(r'^Demo/get_vegetable_by_id/$', get_vegetable_by_id),
    url(r'^Demo/follow_vegetable/$', follow_vegetable),
    url(r'^Demo/report_vegetable_price/$', report_vegetable_price),
    url(r'^Demo/get_reported_price/$', get_reported_price),
    url(r'^Demo/abort_report/$', abort_report),

]
