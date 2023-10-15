from geopy.geocoders import Nominatim
import geocoder
import csv
import random

class Localizacao:

    def __init__(self)->None:
        pass
        
        
    @staticmethod
    def pegar_localizacao()->str:
        
        g = geocoder.ip('me')
        locaizacao = [str(valor) for valor in g.latlng]
        latitude = float(locaizacao[0]) + random.uniform(-0.15, 0.15)
        longitude = float(locaizacao[1]) + random.uniform(-0.15, 0.15)
        with open('./pages/DataSet.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([latitude, longitude, 1])


    def diferencia_localização(self,cordenadas:str)->str:
        
        geolocator = Nominatim(user_agent="testes")
        localizacao = geolocator.reverse(cordenadas)  # Latitude, Longitude
        print(localizacao.address)




print(Localizacao().pegar_localizacao())
