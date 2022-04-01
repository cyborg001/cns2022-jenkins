

from django.urls import path

from . import views

urlpatterns = [
    path("sismos/", views.sismos, name="sismos"),
    path('sismo/',views.sismo, name='sismo'),
    path('articulo/<int:articulo_id>',views.articulo, name='articulo'),
    
    path('', views.inicio, name='inicio'),
    path('register/',views.register, name='register'),
    #Nosotros
    
    path('historia/',views.historia,name='historia'),
    path('definicion/',views.definicion, name='definicion'),
    path('funciones/', views.funciones, name='funciones'),
    path('quienes/',views.quienes, name='quienes'),
    path('base_legal',views.base_legal, name='base_legal'),

    # servicios
    path('lineas/', views.lineas, name= 'lineas'),
    path('proyetos', views.proyectos, name='proyectos'),
    path('acuerdos', views.acuerdos, name='acuerdos'),
    # apis
    path('sismos/sismos_api/',views.sismos_api, name='sismos_api'),
    path('sismo/sismo_api/<int:sismo_id>',views.sismo_api,name='sismo_api'),
    path('uploader/',views.uploader,name='uploader'),
]