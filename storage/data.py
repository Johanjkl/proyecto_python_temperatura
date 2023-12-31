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
        
        case 'Medellin':
            longitud = '75.56359'
            latitud = '6.2518400'
            return longitud, latitud
        
        case 'Barranquilla':
            longitud = '74.7813'
            latitud = '10.9685'
            return longitud, latitud
        
        case _:
            print('No se pudo obtener la temperatura')
            #longitud = '76.5320'
            #latitud = '3.4516'
            #return longitud, latitud
        

def obtener_data(ciudad):
    
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
        return temperatura_celsius
    else:
        print(f'No se pudo obtener la temperatura. Código de estado: {response.status_code}')
        return False

def variar_temperatura(temperatura=10.55):
    #li4 = list(range(-11, 12))
    #print(li4)
    listas_de_temperaturas=[]
    parte_flotante=temperatura%1.0
    for index in range(int(temperatura), int(temperatura + 11)):
        nueva_temperatura=round(index + parte_flotante, 2)
        listas_de_temperaturas.append(nueva_temperatura) 
        #print(index + parte_flotante)
        #print(f'parte_entera es: {parte_flotante:.2f}')
    print(listas_de_temperaturas)
    
    for index in range(int(temperatura - 11), int(temperatura)):
        nueva_temperatura=round(index + parte_flotante, 2)
        listas_de_temperaturas.append(nueva_temperatura) 
        #print(index + parte_flotante)
        #print(f'parte_entera es: {parte_flotante:.2f}')
    listas_de_temperaturas.sort()
    print(listas_de_temperaturas)
    return listas_de_temperaturas

