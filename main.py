from db.base_de_datos import guardar_en_db
from draw.graficar import graficar_temperatura
from storage.data import variar_temperatura, obtener_data


def main():
    temp = obtener_data('Bogota')
    list_temp=variar_temperatura(temp)
    graficar_temperatura(list_temp)
    guardar_en_db()
    return 0

if __name__ == '__main__':
    main()