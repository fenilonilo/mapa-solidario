from geopy.geocoders import Nominatim
import geocoder

class Localizacao:

    def __init__(self) -> None:
        pass


    def pegar_localizacao()->str:
        
        g = geocoder.ip('me')
        locaizacao = ','.join([str(valor) for valor in g.latlng])
        return  locaizacao


    def diferencia_localização(cordenadas:str)->str:
        
        geolocator = Nominatim(user_agent="testes")
        localizacao = geolocator.reverse(cordenadas)  # Latitude, Longitude
        print(localizacao.address)




print(Localizacao.pegar_localizacao())
