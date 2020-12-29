EJERCICIOS DE PYTHON 
PRIMER EJERCICIO
# declaramos la clase persona
class Persona:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 
# declaramos la clase empleado
# la clase empleado hereda los atributos y metodos de la clase Persona
class Empleado(Persona):
    # declaramos el metodo __init__
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 
    # declaramos el metodo mostrar
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)
 
    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no paga impuestos.")

# bloque principal
persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()

Presione Mayús + Tabulación para navegar por el historial de chat.


Mejoramiento del ejercicio anterior
# declaramos la clase persona
class Persona:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 
# declaramos la clase empleado
# la clase empleado hereda los atributos y metodos de la clase Persona
class Empleado(Persona):
    # declaramos el metodo __init__
    def __init__(self):
        # llamamos al metodo init de la clase padre
        # utilizamos la funcion super() para hacer referencia al padre
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
        self.area=input ("Ingrese el area")

    # declaramos el metodo mostrar
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)
        print("Area de trabajo: ",self.area)

    # declaramos el metodo pagar_impuestos
    # comprobara si el empleado debe pagar o no
    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos.")
        else:
            print("El empleado no paga impuestos.")

# bloque principal
persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()


SEGUNDO EJERCICIO
class Vehiculos():
  def __init__(self, marca, modelo):
    self.marca=marca
    self.modelo=modelo
    self.enmarcha=False
    self.acelera=False
    self.frena=False

  def arrancar(self):
    self.enmarcha=True
  def acelerar(self):
    self.acelera=True
  def frenar(self):
    self.frena=True
  def estado(self):
    print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)

class Moto (Vehiculos):
      pass

class Velectricos():
  def __init__(self, carga):
    self.carga=False

  def cargar (self):
    self.carga=true

class Autoelectrico(Vehiculos,Velectricos):
    pass

miAuto= Autoelectrico("Honda","Civic")
miAuto.estado()


TERCER EJERCICIO (POLIMORFISMO)
class coche():
  def desplazamiento(self):
    print("Me desplazo en cuatro ruedas")

class Moto():
  def desplazamiento (self):
    print("Me desplazo en dos ruedas")

class camion():
  def desplazamiento (self):
    print("Me desplazo en seis ruedas")

def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

mivehiculo=Moto()

desplazamientovehiculo(mivehiculo)
ANOTACIONES:
PROXIMA SEMANA EXAMEN 
https://byte-mind.net/curso-python-poo/
staruml.io/download  (descargar para la próxima clase)
youtube.com/watch?v=Z0yLerU0g-Q&ab_channel=LucidchartEspa%C3%B1ol (revisar el video)


