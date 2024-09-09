print("Manejo de funciones V1")
def hola_mundo():
    print("Hola aqui estoy adentro de la funcion")
    
def Mensa(msg):
    print(msg)
def EscribeNC(Nombre,Apellido):
    print(Nombre, Apellido)
    print(f"Tu nombre completo es {Nombre} {Apellido}")
def suma2Numeros(n1,n2):
    s=n1+n2
    return f"La suma de {n1} y de {n2} es de: ", s
# LLamando ala funcion
hola_mundo()
Mensa("Hola Whatsapp") # llama a mensa con 1 parametro
Mensa("El Profe me sorprendio enviando mensajes") # llama a mensa 
EscribeNC("Azul","Torres")

print("Funciones que regresan valores")
print(suma2Numeros(7,3))
print(suma2Numeros(15,45))