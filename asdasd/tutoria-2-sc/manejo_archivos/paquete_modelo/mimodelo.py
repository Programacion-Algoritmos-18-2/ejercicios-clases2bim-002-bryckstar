"""
    creación de clases
"""

class Persona(object):
    """
    """
    # Se crea el metodo __init__ de la clase con todas las variables
    def __init__(self, n, ape, ed, cod, n1, n2):
        """
        """
        self.nombre = n
        self.edad = int(ed)  # Se lo transforma a entero debido a que se lee como string
        self.codigo = int(cod)  # Se lo transforma a entero debido a que se lee como string
        self.apellido = ape
        self.nota1 = int(n1)  # Se lo transforma a entero debido a que se lee como string
        self.nota2 = int(n2)  # Se lo transforma a entero debido a que se lee como string

    # Se crean los metodos agregar y obtener para las variables
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_nota1(self, n):
        self.nota1 = n

    def obtener_nota1(self):
        return self.nota1
    
    def agregar_nota2(self, n):
        self.nota2 = n

    def obtener_nota2(self):
        return self.nota2

    # Se crea el metodo para presentar los datos
    def __str__(self):
        """
        """
        return "%s - %s - %d - %d -%d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.obtener_nota1(), self.obtener_nota2())

# Se crea la clase para operar con las personas
class OperacionesPersona(object):
    """
    """
    # Se crea el metodo __init de la clase
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado

    # Se crea el metodo para imprimir los datos
    def __str__(self):
        c = ''
        for i in self.listado_personas:
            c = "%s %s %s\n" % (c, i.obtener_nombre(), i.obtener_apellido())
        return c

    
    # Se crea el metodo para retornar los alumnos con nota 1 menor a 15
    def obtener_listado_n1(self):
        suma = 0
        c = 'Los estudiantes con nota 1 menor a 15 son:\n'  # Se inicializa el encabezado
        for i in self.listado_personas:
            if(i.obtener_nota1() < 15):
                c = "%s%s %s" % (c, i.obtener_nombre(), i.obtener_apellido())  # Se agregan los datos a la cadena
        return c

    # Se crea el metodo para retornar los alumnos con nota2 menor a 15
    def obtener_listado_n2(self):
        suma = 0
        c = 'Los estudiantes con nota 2 menor a 15 son:\n'
        for i in self.listado_personas:
            if(i.obtener_nota2() < 15):
                c = "%s%s %s" % (c, i.obtener_nombre(), i.obtener_apellido())
        return c


    # Se crea el metodo para retornar las personas que su nombre empiece con algun caracter especifico
    def obtener_listado_personas(self, n, m):  # Se reciben dos parametros
        c = 'Los nombres de los estudiantes que empiezan con %s y %s son:\n' % (n, m)
        for x in self.listado_personas:
            if (n == x.obtener_nombre()[0] or m == x.obtener_nombre()[0]):  # Se compara si la primera letra del nombre es igual al caracter recibido en el metodo
                c = "%s%s\n" % (c, x.obtener_nombre())
        return c

    
    # Se crea el metodo para obtener el promedio de las notas 1
    def obtener_promedio_n1(self):
        suma = 0
        for n in self.listado_personas:
            suma +=  n.obtener_nota1()
        return suma/len(self.listado_personas)

    # Se crea el metodo para obtener el promedio de las notas 1
    def obtener_promedio_n2(self):
        suma = 0
        for n in self.listado_personas:
            suma +=  n.obtener_nota2()
        return suma/len(self.listado_personas) 