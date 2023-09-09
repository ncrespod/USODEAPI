from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import mysql.connector
import requests
server = "sql177.main-hosting.eu"
bd = "u153713658_productos"
userw = "u153713658_web"
password = "Productosweb123"

class Reg(View):
	template_name = "tables-simple.html"

	def get(self, request):	
		
		if request.method == "GET":
			
			url = "https://fakestoreapi.com/products"

			try:
				con = mysql.connector.connect(
					host = server, user = userw, passwd = password, database = bd
					)
				cur = con.cursor()

				# Realiza la solicitud GET
				response = requests.get(url)

				# Verifica si la solicitud fue exitosa (código de estado 200)
				if response.status_code == 200:
					# La respuesta de la API está en formato JSON
					data = response.json()

					# Itera a través de los productos y los inserta en la base de datos
					for product in data:
						# Obtén los datos específicos del producto
						product_id = product['id']
						nombre = product['title']
						precio = product['price']
						descripcion = product['description']
						categoria = product['category']
						imagen = product['image']
						
						# Consulta SQL para insertar un producto
						insert_query = "INSERT INTO productosweb (id, nombre, precio, descripcion, categoria, imagen) VALUES (%s, %s, %s, %s, %s, %s)"
						values = (product_id, nombre, precio, descripcion, categoria, imagen)

						# Ejecuta la consulta
						cur.execute(insert_query, values)

					# Confirma los cambios en la base de datos
					con.commit()

					print("Los datos se han insertado en la base de datos con éxito.")
				else:
					print(f"Error en la solicitud. Código de estado: {response.status_code}")

			except requests.exceptions.RequestException as e:
				print(f"Error en la solicitud: {e}")
			except mysql.connector.Error as err:
				print(f"Error en la base de datos: {err}")
			finally:
				# Cierra el cursor y la conexión
				cur.close()
				con.close()

		

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
		
		return render(request, self.template_name, { "data2": datos})

	
