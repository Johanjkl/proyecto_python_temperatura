import matplotlib.pyplot as plt

def graficar_temperatura(datos):
    print("Soy graficar temperatura")


    # Crear una lista de etiquetas para el eje x (puedes personalizarlas)
    etiquetas1 = ['Día 1', 'Día 2', 'Día 3', 'Día 4', 'Día 5', 'Día 6', 
                  'Día 7', 'Día 8', 'Día 9', 'Día 10', 'Día 11']
    etiquetas2 = ['Día 12', 'Día 13', 'Día 14', 'Día 15', 'Día 16', 'Día 17', 
                  'Día 18', 'Día 19', 'Día 20', 'Día 21', 'Día 22']
    etiquetas = etiquetas1 + etiquetas2
    print(etiquetas)
    plt.xticks(rotation=45)

    # Crear un gráfico de barras
    plt.bar(etiquetas, datos)

    # Agregar etiquetas al gráfico
    plt.xlabel('Dias')
    plt.ylabel('Temperatura')

    # Agregar un título al gráfico
    plt.title('Temperaturas')

    # Mostrar el gráfico
    plt.show()

    return True