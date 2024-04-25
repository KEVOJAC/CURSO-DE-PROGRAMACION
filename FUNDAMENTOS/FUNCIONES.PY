def saludar():
    print("Hello!")

saludar()

def saludar2(nombre):
    print("Hello, ",nombre)

saludar2("Diego")
saludar2("Angel")
saludar2("Kevin")

def area(x):
    area1=3.14*x**2
    print("El area de un circulo es: ",area1)

x=int(input("Ingrese el radio: "))
area(x)


def suma(nombre):
    print("la suma es: ",nombre)

x2=int(input("Ingrese un numero: "))
x1=int(input("Ingrese un numero: "))
area1=x1+x2
suma(area1)

def DATOS(nombre,edad,estatura):
    print("El nombres es: ",nombre)
    print("La edad es: ",edad)
    print("La estatura es de: ",estatura)

nom=(input("Ingrese su nombre: "))
eda=int(input("Ingrese su edad: "))
esta=(input("Ingrese su estatura: "))
DATOS(nom,eda,esta)

def Grados(Celsius):
    print("De Celsius a Fahrenheit: ",Celsius)
def Grados1(Fahrenheit):
    print("La edad es: ",Fahrenheit)

nom=float(input("Ingrese los grados celsius: "))
fahr=nom*(9/5)+32
Grados(fahr)
eda=float(input("Ingrese los grados Fahrenheit: "))
cels=(eda-32)*(5/9)
Grados1(cels)