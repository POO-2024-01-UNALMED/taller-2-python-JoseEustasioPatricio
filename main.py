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
        

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = ""
        self.precio = 0
        self.asientos = Asiento = []
        self.marca = ""
        self.motor = Motor
        self.registro = 0
        self.cantidadCreados = cantidadCreados

    def cantiadAsientos (self):
        return(len(Asiento))

    def verificarIntegridad ():
        if Motor.registro == Auto.registro == Asiento.registro:
            print("Auto Original")
        else:
            print("Las piezas no son originales")
