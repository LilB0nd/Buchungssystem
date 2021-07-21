"""Praktikum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Buchungssystem.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', SignUP.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', SignUP.activate, name='activate'),
    path('equipment/', EquipmentView.as_view(), name='equipment'),
    url(r'^Device/(?P<pk>.+)/$', DeviceView.as_view(), name='Device'),
    path('users/', Usersview.as_view(), name='Lehreransicht'),
    url(r'^user/(?P<pk>.+)/$', Userview.as_view(), name='User'),
    path('calendar/', Appoinment.as_view(), name='calender1'),
    path('', IndexView.as_view(), name='Index'),

    #path('course/', IntroductionCourse.as_view(), name='IntroductionCourse')
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)