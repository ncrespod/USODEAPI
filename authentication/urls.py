# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from cgitb import html
from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from registros.views import Reg
from registros import views
from django.conf.urls.static import static 
from datos.views import ReportePersonalizadoExcel


urlpatterns = [
   
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("Registros/", Reg.as_view(), name="tables-simple"),
    path('reporte/',ReportePersonalizadoExcel.as_view(), name = 'reporte'),

    
]
