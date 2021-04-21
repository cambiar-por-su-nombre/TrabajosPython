print('hola mundo')

archivo  = open('palabras500.csv', encoding="utf-8")
lineas = archivo.readlines()
archivo.close()

print(len(lineas))

print(lineas[0])

print(lineas)