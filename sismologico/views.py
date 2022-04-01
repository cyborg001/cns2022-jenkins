from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import time
import os
from datetime import datetime, date
from .models import User, Sismo, Article
import requests
from capstone.settings.base import *
# Create your views here.

import threading
if User.objects.all().exists():
        analista = User.objects.filter(username='carlos')[0]
else:
    analista = User(username='carlos',email='cgrs27@gmail.com')
    analista.save()
path= r'C:\Users\cgrs27\Desktop\tk_hyper_noel\dummyX.dat'
data = ''
temp = ''

def set_estilo(fecha,hora):
    '''esta funcion acepta la fecha y hora del sismo para calcular
        el estilo que llevara el icono relacionado al circulo en el mapa
        mientras mas reciente mas tiende al rojo'''
    y = int(fecha[0:4])
    month = int(fecha[5:7])
    day = int(fecha[8:10])
    h = int(hora[0:2])
    minu = int(hora[3:5])
    sec = int(hora[6:8])
    now = int(datetime.timestamp(datetime.now()))
    tiempo = int(datetime.timestamp(datetime(y,month,day,h,minu,sec)))
    t = (now - tiempo)/3600
    # print(t)
    if t >= 6:
       
        return {
            'fillColor':'green',
            'color':'green',
            'fillOpacity':'0.2',
        }
    elif t >= 3:
        return {
            'fillColor':'yellow',
            'color': 'yellow',
            'fillOpacity':'0.2',
        }
    elif t >=1:
        return {
            'fillColor':'orange',
            'color':'orange',
            'fillOpacity':'0.2',
        }
    else:
        return {
            'fillColor':'red',
            'color':'red',
            'fillOpacity':'0.2',
        }

def register(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "sismologico/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, password)
            user.save()
        except IntegrityError:
            return render(request, "sismologico/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("inicio"))
    else:
        return render(request, 'sismologico/register.html')


def sismos(request):
   
    return render(request,'sismologico/sismos.html')


def sismo_api(request,sismo_id):
    '''crea el api para sismos individuales segun sismo_id'''
    
    sismo = Sismo.objects.filter(pk=int(sismo_id))
    if len(sismo) > 0:
        sismo = Sismo.objects.get(pk=sismo_id).serialize()
        # print(sismo['data_estaciones'])
        sismo = parse_geojson([sismo])
        
        return JsonResponse({'sismo':sismo})

def inicio(request):
    articles = Article.objects.order_by('-date').all()
    articles = [article.serialize() for article in articles]
    print(articles)
    return render(request,'sismologico/inicio.html',{'articles':articles})

def sismos_api(request):

    ''' utilizarlo para cargarlo a 
        la pagina y guardarlo en la base de datos interna de la 
        pagina y eliminarlo terminado el proceso.'''
   
    print(threading.current_thread())
    sismos = Sismo.objects.order_by('-custom_id').all()
    # for n in sismos:
    #     n.analista='carlos'
    #     n.save()
    sismos = [sismo.serialize() for sismo in sismos][:20]
    # print(sismos)
    geojson = parse_geojson(sismos)
    # print(geojson)
    # return HttpResponse(f'el thread activo es {current}')
    return JsonResponse({'geojson':geojson,
                        })
    
def parse_geojson(sismos):
    # '''turn data into geoJson format'''
    if sismos:
        features = []
        for sismo in sismos:
            estilos = set_estilo(str(sismo['fecha']),str(sismo['hora']))
            features.append({
                        'type':'Feature',
                        'geometry':{
                            'type':'Point',
                            "coordinates":[sismo['longitud'],sismo['latitud']],
                        },
                        'properties':{
                            'analista':[sismo['analista'],False],
                            'fecha':[sismo['fecha'],True],
                            'hora':[sismo['hora'],True],
                            'latitud':[sismo['latitud'],True],
                            'longitud':[sismo['longitud'],True],
                            'magnitud':[float(sismo['magnitud']),True],
                            'profundidad':[sismo['profundidad'],True],
                            'comentario':[sismo['comentario'],True],
                            'id':[sismo['id'],False],
                            'custom_id':[sismo['custom_id'],False],
                            'tr_id':'tr_'+str(sismo['id']),
                            'magC':[sismo['magC'],False],
                            'magL':[sismo['magL'],False],
                            'magW':[sismo['magW'],False],
                            'rms':[sismo['rms'],False],
                            'sentido':[sismo['sentido'],False],
                            'strGap':[sismo['gapInfo'],False],
                            'strFocal':[sismo['focalInfo'],False],
                            'data_estaciones':[sismo['data_estaciones'],False],
                            'estilos':estilos,

                        }
                        
                    })
        geojson ={'type':'FeatureCollection',
                'features':features,}
        return geojson

def sismo(request):
    if request.method=='GET':
        id = int(request.GET.get('id'))
        lat = request.GET.get('latitud')
        lon= request.GET.get('longitud')
        return render(request,'sismologico/sismo.html',{'id':id,
                                                        'lat':lat,
                                                        'lon':lon,
                                                        })

def quienes(request):
    return render(request,'sismologico/quienes.html')

def base_legal(request):
    return render(request, 'sismologico/base_legal.html')

def historia(request):
    return render(request,'sismologico/historia.html')

def definicion(request):
    return render(request, 'sismologico/definicion.html')

def funciones(request):
    return render(request, 'sismologico/funciones.html')

def lineas(request):
    return render(request, 'sismologico/lineas.html')

def proyectos(request):
    return render(request, 'sismologico/proyectos.html')

def acuerdos(request):
    return render(request, 'sismologico/acuerdos.html')

def validar_fecha(fecha,hora):
    '''esta funcion acepta la fecha y hora del sismo para calcular
        el estilo que llevara el icono relacionado al circulo en el mapa
        mientras mas reciente mas tiende al rojo'''
    y = int(fecha[0:4])
    month = int(fecha[5:7])
    day = int(fecha[8:10])
    h = int(hora[0:2])
    minu = int(hora[3:5])
    sec = int(hora[6:8])
    now = int(datetime.timestamp(datetime.now()))
    tiempo = int(datetime.timestamp(datetime(y,month,day,h,minu,sec)))
    t = (now - tiempo) 
    if t >0:
        return True
    return False

def uploader(request):
    print(request,'datos')
    if request.headers['Token'] != get_secret('CUSTOM_TOKEN'):
        print('el token no coincide')
        return HttpResponse({'error':'El token no concuerda'})
    print('token correcto')
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        if validar_fecha(data['fecha'],data['hora']):
            print(f"Fecha ({data['fecha']} {data['hora']}) validada")
            sismo_actual =Sismo.objects.filter(custom_id=data['id'])
            
            if sismo_actual:
                sismo_actual.delete()
            print(data['lat'])
            sismo = Sismo(analista=data['analista'],user=analista,custom_id=data['id'],
            fecha=data['fecha'],hora=data['hora'],latitud=data['lat'],
            longitud=data['lon'],profundidad=data['depth'],magnitud=data['mag'],
            comentario=data['comentario'],magC=data['magC'],magL=data['magL'],
            magW=data.get('magW'),gapInfo=data['gapInfo'],focalInfo=data['focalInfo'],
            sentido=data['sentido'],data_estaciones=data['data_estaciones'],rms=data['rms'],)

            print('sismo subido')
            sismo.save()
        else:
            print('Fecha incorrecta')
        return render(request,'sismologico/sismos.html')

    else:
        print('es get')
        return HttpResponse('es get')

        
def articulo(request, articulo_id):
    s = ''
    articulo = Article.objects.get(pk=int(articulo_id)).serialize()
    if '\n\n' in articulo['content']:
        articulo['content'] = articulo['content'].split('\n\n')
    elif '\r\n\r' in articulo['content']:
        articulo['content'] = articulo['content'].split('\r\n\r')
    for n in articulo['content']:
        if '\n' in n:
            print(n)
            n = n.replace('\n','')
            
    print(articulo['content'])
    return render(request,'sismologico/articulo.html',{'articulo':articulo})