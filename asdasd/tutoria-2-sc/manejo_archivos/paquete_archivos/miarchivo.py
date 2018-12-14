import codecs
import sys


# Se crea la clase mi archivo para obtener los datos
class MiArchivo:
    """
    """
    
    def __init__(self):  # Se crea el metodo __init__
        """
        """
        self.archivo = codecs.open("data/demo_notas.csv", "r")  # Se declara el archivo con los datos del archivo

    # Se crea el metodo para obtener la informacion del archivo
    def obtener_informacion(self):
        return self.archivo.readlines()

    # se crea el metodo para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo))

    def cerrar_archivo(self):
        self.archivo.close()
