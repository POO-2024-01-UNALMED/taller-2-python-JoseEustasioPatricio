class Asiento:
    def __init__(self, color, precio, registro):
        self.color = "" 
        self.precio = 0
        self.registro = 0
    
    def cambiarColor(self, color):
        coloreAceptado = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in coloreAceptado :
            self.color = color

class Motor:
    def __init__(self, numeroCiindros, tipo, registro):
        self.numeroCiindros = 0
        self.tipo = ""
        self.registro = 0

    def cambiarRegistro (self, registro):
        self.registro = registro

    def asignarTipo (self, tipo):
        if tipo == ("electrico" or "gasolina"):
            self.tipo = tipo
        else:
            self.tipo = self.tipo
        

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = ""
        self.precio = 0
        self.asientos = Asiento = []
        self.marca = ""
        self.motor = Motor
        self.registro = 0

    def cantidadAsientos (self):
        return(len(Asiento))

    def verificarIntegridad ():
        a = True
        for i in Asiento:
            if Motor.registro == Auto.registro == i.registro:
                a = True
            else:
                a = True
        if a == True:
            print("Auto original")
        else: 
            print("Las piezas no son originales")
