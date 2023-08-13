import matplotlib.pyplot as plt  # Importa la biblioteca Matplotlib para gráficos

def generate_pie_chart():
    # Etiquetas y valores para el gráfico de pastel
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    # Crea una figura y ejes para el gráfico
    fig, ax = plt.subplots()

    # Genera el gráfico de pastel con valores y etiquetas
    ax.pie(values, labels=labels)

    # Guarda la figura como un archivo PNG
    plt.savefig('pie.png')

    # Cierra la figura para liberar recursos
    plt.close()

