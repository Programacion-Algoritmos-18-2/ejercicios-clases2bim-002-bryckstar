from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]  # Se inicializa la lista en la posicion 1
lista_personas = []  # Se inicia la lista vacia

# Se crea un ciclo para recorrer la lista de personas
for d in lista:
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])  # Se llama al metodo Persona y se le agregan los datos
    lista_personas.append(p)  # Se agregan datos a la lista vacia

operaciones = OperacionesPersona(lista_personas)  # Se llama el metodo OperacionesPersonas y se le agregan los datos
print(operaciones)  # Se imprimen los datos 
print(operaciones.obtener_promedio_n1())  # Se imprime el promedio de notas 1
print(operaciones.obtener_promedio_n2())  # Se imprime el promedio de notas 2
print(operaciones.obtener_listado_n1())  # Se imprimen los estudiantes con nota 1 menor a 15
print(operaciones.obtener_listado_n2())  # Se imprimen los estudiantes con nota 2 menor a 15
print(operaciones.obtener_listado_personas("R", "J"))  # Se imprimen los nombres de los estudiantes que empiecen con R o J