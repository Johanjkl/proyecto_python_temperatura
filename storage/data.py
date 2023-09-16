import requests
#API_KEY = 'cdd4b936b4fb62516f1493373505e369'
API_KEY = 'cdd4b936b4fb62516f1493373505e369'


def coordenadas(ciudad):
    match ciudad:
        case 'Bogota':
            longitud = '74.0721'
            latitud = '4.7110'
            return longitud, latitud
        
        case 'Cali':
            longitud = '76.5320'
            latitud = '3.4516'
            return longitud, latitud
        
        case _:
            longitud = '76.5320'
            latitud = '3.4516'
            return longitud, latitud
        

def obtener_data(ciudad='Cali'):
    
    long, lati = coordenadas(ciudad)
    print(long, lati)
    print(f"Soy obtener data {ciudad}")
    # URL de la API de OpenWeatherMap
    #url = f'http://api.openweathermap.org/data/2.5/weather?q=CIUDAD&appid={API_KEY}'    
    
    

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lati}&lon={long}&appid={API_KEY}'    
    # Realiza la solicitud HTTP a la API
    response = requests.get(url).json()
    #print(type(response))
    print(response.keys())
    #print(response.cod)
    print(response['cod'])
    

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response['cod'] == 200:
        data = response
        # Obtiene la temperatura en grados Celsius desde los datos JSON
        temperatura_celsius = data['main']['temp'] - 273.15
        print(f'Temperatura actual en {ciudad}: {temperatura_celsius:.2f}°C')
    else:
        print(f'No se pudo obtener la temperatura. Código de estado: {response.status_code}')
    
    return True

def extraer_temperatura():
    print("Soy extraer temperatura")
    return False

