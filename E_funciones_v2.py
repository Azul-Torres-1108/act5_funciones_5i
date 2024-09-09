print("funciones creadas por el usuario")

def Mi_Lista():
    amigos=["Diana", "Andy", "Leysi"]
    for azul in amigos:
        print(azul)
# llamadas a funciones
Mi_Lista()
#Tuplas
print("Mis tuplas:")
numeros=(1,2,3,4)
print(numeros)
print("-rango de numeros")
print(numeros[3])
y = list(numeros)
y[1] = "5"
x = tuple(y)
print(x)
for num in numeros:
    print(num)
# Mi Diccionario
print("Mi diccionario:")
diccionario = {
    "Dia": 10,
    "mes": "Enero",
    "año": "2024",
    "colores": ["Azul", "Lila", "Amarillo"]
}
print(diccionario)
for x in diccionario:
    print(x)
    print(diccionario[x])
# Mis Conjuntos
print("Mis conjuntos:")
animales=("Huron", "Gato", "Perico", "Pantera")
print(animales)

for x in animales:
    print(x)