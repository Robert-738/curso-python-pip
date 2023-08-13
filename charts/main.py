import charts  # Importa el módulo "charts"

def run():
    charts.generate_pie_chart()  # Llama a la función para generar el gráfico de pastel

if __name__ == '__main__':
    run()  # Ejecuta la función "run()" si este archivo es ejecutado directamente



'''
if __name__ == '__main__':
    Esta línea verifica si el archivo "main.py" está siendo ejecutado directamente 
    (no importado como un módulo en otro archivo). Esto es útil para evitar que el código 
    en este bloque se ejecute cuando se importa el archivo en otro lugar.

run(): 
Si el archivo está siendo ejecutado directamente, esta línea llama a la función "run()", 
que a su vez llama a "charts.generate_pie_chart()". Esto inicia la generación de un gráfico circular.
'''