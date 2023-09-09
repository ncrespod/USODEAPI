from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse, JsonResponse
import csv 
import pandas as pd
from firebase_admin import db
import mysql.connector
import requests
server = "sql177.main-hosting.eu"
bd = "u153713658_productos"
userw = "u153713658_web"
password = "Productosweb123"
class ReportePersonalizadoExcel(TemplateView):
    def get(self,request,*args,**kwargs):

        try:
            con = mysql.connector.connect(
                host = server, user = userw, passwd = password, database = bd
                )
            cur = con.cursor()
            sql = sql = "SELECT * FROM productosweb"
            print(sql)
            cur.execute(sql)           
            datos =  cur.fetchall()
            print(datos)
            if datos is None:
                print("El registro no existe")
            else:
                print("El registro existe y sus datos son:", datos)
                            
            
            cur.close
        except:
            pass

        
        field_names = ['id','Productos', 'Descripcion','Categoria','Precio','Imagen' ] 
        # Convierte los datos de tuplas a diccionarios
        datos_dict = []
        for dato in datos:
            datos_dict.append({
                'id': dato[0],
                'Productos': dato[1],
                'Descripcion': dato[2],
                'Categoria': dato[4],
                'Precio': dato[3],
                'Imagen': dato[5]
            })

        with open('Names.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for dato in datos_dict:
                writer.writerow(dato)
           
    
        nombre_archivo = "ReporteProductos.xlsx"
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        df = pd.read_csv('Names.csv',encoding='latin-1')
        df.to_excel(response, index=False)
        return response
