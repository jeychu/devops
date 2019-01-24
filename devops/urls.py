"""devops URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from idcs.views import IdcViewSet
from users.views import UserViewset
from cabinet.views import CabinetViewSet
from manufacturer.views import ManufacturerViewset, ProductModelViewset
from servers.views import ServerAutoReportViewset, NetworkDeviceViewset, IPViewset, ServerViewset

route = DefaultRouter()
route.register("idcs", IdcViewSet, base_name="idcs")
route.register("users", UserViewset, base_name="users")
route.register("cabinet", CabinetViewSet, base_name="cabinet")
route.register("manufacturer", ManufacturerViewset, base_name="manufacturer")
route.register("productModel", ProductModelViewset, base_name="productModel")
route.register("serverAutoReport", ServerAutoReportViewset, base_name="serverAutoreports")
route.register("servers", ServerViewset, base_name="Servers")
route.register("networkDevice", NetworkDeviceViewset, base_name="networkDevice")
route.register("IP", IPViewset, base_name="IP")

urlpatterns = [
    url(r'^', include(route.urls)),
    url(r'^docs/', include_docs_urls("51reboot devops platform documents"))
]
