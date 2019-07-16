"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api.views import LoginAuthView,LoginShowView,LoginView
from assets.views import CmdbView,CmdbDeleteView,CollectHostInfo,AssetsView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/login_auth/', LoginAuthView),
    url(r'^api/login/', LoginShowView),
    url(r'^api/auth/', LoginView),
    url(r'^api/v1/cmdb$', CmdbView.as_view(), name='cmdb_list'),
    url(r'^api/v1/cmdb/delete/(?P<pk>[0-9]+)/$', CmdbDeleteView),
    url(r'^api/v1/cmdb/collect', CollectHostInfo.as_view()),

    url(r'^assets/(?P<year>[0-9]{4})/$', AssetsView, name='book_year')
]
