#2D ARRAY
#print as usual
countries = {'Germany': ['Berlin', 83], 'Belgium': ['brussels', 23], 'Ireland': ['Dublin', 11]}
city = countries['France'][1]
print(city)

#delete data
del countries['Germany'][0]
print(countries)

#change data
countries['Belgium'][0] = 'brazil'
countries['Ireland'][1] = 90
print(countries)

#1D ARRAY
results = {'deta': 17, 'Nova': 84}
score = results ['deta']
print(score)

#delete data
del results['deta']
print(results)

#change data
results['Nova'] = 100
print(results)

#add data
results ['hazni'] = 101
print(results)
