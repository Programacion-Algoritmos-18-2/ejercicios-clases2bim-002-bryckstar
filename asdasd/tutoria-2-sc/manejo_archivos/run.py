from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
sum_n1 = 0  # Se inicializa suman1 en 0
sum_n2 = 0  # Se inicializa suman2 en 0
for d in lista:
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])  # Se agregan datos
    
    if (p.obtener_nota1() < 15 or p.obtener_nota2() < 15):
    	print(p.obtener_nombre())  # Se imprimen los estudiantes con notas menores a 15
    
    sum_n1 += p.obtener_nota1()  # Se suman los datos de las notas 1
    sum_n2 += p.obtener_nota2()  # Se suman los datos de las notas 2
   

# Se calculan los promedios
prom_n1 = sum_n1/len(lista) 
prom_n2 = sum_n2/len(lista)
print(prom_n1)
print(prom_n2)