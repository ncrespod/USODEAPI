from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View 
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import mysql.connector
import requests

class Reg2(View):
    template_name = "tables-simple2.html"
    
    def get(self, request):	
        if request.method == "GET":
            url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMWY0OWU4MGM3ZjEyNmM3NDNiN2I1OGExYmIwY2ZmYyIsInN1YiI6IjY1MWEyMDRlYzUwYWQyMDBjOTFiYzNlMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.AcsjeG0upiegYhzcaHRMdAxpbgF_v73pst3EgvP8Das"
            }

            response = requests.get(url, headers=headers)
            data = response.json()

            # Obtén la lista de resultados y selecciona solo los campos requeridos
            resultados = data.get("results", [])
            print(resultados)
            peliculas = [{"original_title": pelicula["original_title"], "popularity": pelicula["popularity"],
                        "vote_average": pelicula["vote_average"], "vote_count": pelicula["vote_count"],"release_date": pelicula["release_date"],"overview": pelicula["overview"]}
                        for pelicula in resultados]
            print(peliculas)
            # Renderiza la lista en una plantilla Django
        return render(request, self.template_name, {"peliculas": peliculas})
   