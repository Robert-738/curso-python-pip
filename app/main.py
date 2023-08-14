import utils
import read_csv
import charts


#Seleccionar columna world population percentage

def run():
    data = read_csv.read_csv('data.csv') #obtenemos la informacion csv en el formato en forma de diccionario
    data=list(filter(lambda item: item['Continent'] == 'South America', data)) #filtramos solo paises de suramerica

    countries= list(map(lambda x: x['Country/Territory'], data)) #filtramos con map la columna country para obtener los paises
    percentages= list(map(lambda x: x['World Population Percentage'], data)) #filtramos con map los porcentajes
    charts.generate_pie_chart(countries, percentages) #generamos piechart


    country= input('Type country=> ')
    print(country)

    result = utils.population_by_country(data,country.capitalize())

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
    run()

