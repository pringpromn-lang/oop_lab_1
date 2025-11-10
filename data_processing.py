import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


def filter_dicts(condition, dict_list):
    return [item for item in dict_list if condition(item)]

def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [float(item[aggregation_key]) for item in dict_list]
    return aggregation_function(values) if values else None


#Average temperature of all cities
print("Average temperature of all the cities:")
avg_temp = aggregate('temperature', lambda x: sum(x)/len(x), cities)
print(avg_temp)
print()

#All cities in Germany
print("All cities in Germany:")
germany_cities = filter_dicts(lambda x: x['country'] == 'Germany', cities)
for city in germany_cities:
    print(city['city'])
print()

#All cities in Spain with temperature above 12°C
print("All cities in Spain with temperature above 12°C:")
spain_hot = filter_dicts(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
for city in spain_hot:
    print(city['city'])
print()

#Number of unique countries
countries = set(city['country'] for city in cities)
print("Number of unique countries:", len(countries))
print()

#Average temperature for all the cities in Germany
print("Average temperature for cities in Germany:")
avg_germany_temp = aggregate('temperature', lambda x: sum(x)/len(x), germany_cities)
print(avg_germany_temp)
print()

#Max temperature for all the cities in Italy
print("Max temperature for cities in Italy:")
italy_cities = filter_dicts(lambda x: x['country'] == 'Italy', cities)
max_italy_temp = aggregate('temperature', lambda x: max(x), italy_cities)
print(max_italy_temp)
print()
