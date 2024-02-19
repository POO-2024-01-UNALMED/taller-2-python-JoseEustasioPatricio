class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color 
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        coloreAceptado = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in coloreAceptado :
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCiindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro (self, registro):
        self.registro = registro

    def asignarTipo (self, tipo):
        if tipo == ("electrico" or "gasolina"):
            self.tipo = tipo
        

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos (self):
        asientos = self.asientos
        cantidad = 0
        for elemento in asientos:
            if isinstance(elemento, Asiento) == True:
                cantidad += 1
        return cantidad
        

    def verificarIntegridad ():
        if (self.registro == self.motor.registro):
            for asiento in self.asientos
                if asiento.registro != self.registro:
                    return"Las piezas no son originales"
                else:
                    return"Auto original"
        return"Las piezas no son originales"




        #return"Las piezas no son originales"
        #return "Auto original"
