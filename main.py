from db.base_de_datos import guardar_en_db
from draw.graficar import graficar_temperatura
from storage.data import extraer_temperatura, obtener_data


def main():
    obtener_data()
    extraer_temperatura()
    graficar_temperatura()
    guardar_en_db()
    return 0

if __name__ == '__main__':
    main()