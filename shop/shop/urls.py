"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from header.views import(header_view, shop_view, login_view, detail_view, contact_view, checkout_view, cart_view, blog_view,
    blog_single_view, page_404_view)

urlpatterns = [

    url(r'^$', header_view),
    url(r'^shop/$', shop_view),
    url(r'^detail/$', detail_view),
    url(r'^login/$', login_view),
    url(r'^contact/$', contact_view),
    url(r'^checkout/$', checkout_view),
    url(r'^cart/$', cart_view),
    url(r'^blog/$', blog_view),
    url(r'^blog-single/$', blog_single_view),
    url(r'^404/$', page_404_view),
    url(r'^admin/', admin.site.urls),
]
