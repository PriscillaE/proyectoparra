"""ProyectoSepher URL Configuration

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
from django.contrib.auth.views import login, logout_then_login
from home.views import Index_view,Registro_paciente,Reporte_Paciente,EditarPaciente,Paciente_detalle,Registro_Historial
from home.views import Registro_Minutas,Detalle_minuta,Reporte_Minutas,Registro_Apoyo,Registro_Defunciones
from home.views import Reporte_Defunciones,Eliminar_Defunciones,Registro_Eventos,Eliminar_Eventos,Reporte_Eventos
from home.views import Detalle_eventos,Registro_Personal,Eliminar_Personal,Editar_Personal,Reporte_Personal,Editar_Evento

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',Index_view.as_view(),name='Index_view'),
    url(r'^registro_paciente/$',Registro_paciente.as_view(),name='RegistroPac_view'),
    url(r'^reporte_pacientes/$',Reporte_Paciente.as_view(),name='ReportePac_view'),
   	url(r'^editar_paciente/(?P<pk>\d+)$',EditarPaciente.as_view(),name='editar_paciente_view'),
   	url(r'^detalle_paciente/(?P<pk>\d+)$',Paciente_detalle,name='paciente_detalle_view'),
   	url(r'^registro_medico/$',Registro_Historial.as_view(),name='RegistroMed_view'),
   	url(r'^registro_minutas/$',Registro_Minutas.as_view(),name='RegistroMin_view'),
   	url(r'^detalle_minuta/(?P<pk>\d+)$',Detalle_minuta.as_view(),name='DetalleMin_view'),
   	url(r'^reporte_minutas/$',Reporte_Minutas.as_view(),name='ReporteMin_view'),
   	url(r'^registro_defunciones/$',Registro_Defunciones.as_view(),name='RegistroDef_view'),
   	url(r'^registro_apoyo/$',Registro_Apoyo.as_view(),name='RegistroApy_view'),
   	url(r'^reporte_defunciones/$',Reporte_Defunciones.as_view(),name='ReporteDef_view'),
   	url(r'^eliminar_defunciones/(?P<pk>\d+)$',Reporte_Defunciones.as_view(),name='EliminarDef_view'),
   	url(r'^registro_eventos/$',Registro_Eventos.as_view(),name='RegitroEve_view'),
   	url(r'^eliminar_eventos/(?P<pk>\d+)$',Eliminar_Eventos.as_view(),name='EliminarEve_view'),
   	url(r'^editar_evento/(?P<pk>\d+)$',Editar_Evento.as_view(),name='editar_evento_view'),
   	url(r'^reporte_eventos/$',Reporte_Eventos.as_view(),name='ReporteEve_view'),
   	url(r'^detalle_evento/(?P<pk>\d+)$',Detalle_eventos.as_view(),name='DetalleEve_view'),
   	url(r'^registro_personal/$',Registro_Personal.as_view(),name='RegitroPer_view'),
   	url(r'^eliminar_personal/(?P<pk>\d+)$',Eliminar_Personal.as_view(),name='EliminarPer_view'),
   	url(r'^editar_personal/(?P<pk>\d+)$',Editar_Personal.as_view(),name='editar_personal_view'),
   	url(r'^reporte_personal/$',Reporte_Personal.as_view(),name='ReportePer_view'),
]

