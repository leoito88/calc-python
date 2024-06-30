import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b):
    return math.pow(a, b)

def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz cuadrada de un número negativo"
    return math.sqrt(a)

def logaritmo(a, base=math.e):
    if a <= 0:
        return "Error: Logaritmo de un número no positivo"
    return math.log(a, base)

def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def calculadora():
    print("Bienvenido a la calculadora avanzada")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Logaritmo")
    print("8. Seno")
    print("9. Coseno")
    print("10. Tangente")
    
    operacion = input("Ingrese el número de la operación deseada: ")

    if operacion in ['1', '2', '3', '4', '5']:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        if operacion == '1':
            print(f"Resultado: {suma(a, b)}")
        elif operacion == '2':
            print(f"Resultado: {resta(a, b)}")
        elif operacion == '3':
            print(f"Resultado: {multiplicacion(a, b)}")
        elif operacion == '4':
            print(f"Resultado: {division(a, b)}")
        elif operacion == '5':
            print(f"Resultado: {potencia(a, b)}")
    elif operacion == '6':
        a = float(input("Ingrese el número: "))
        print(f"Resultado: {raiz_cuadrada(a)}")
    elif operacion == '7':
        a = float(input("Ingrese el número: "))
        base = input("Ingrese la base del logaritmo (presione Enter para usar base e): ")
        if base:
            base = float(base)
            print(f"Resultado: {logaritmo(a, base)}")
        else:
            print(f"Resultado: {logaritmo(a)}")
    elif operacion == '8':
        a = float(input("Ingrese el ángulo en grados: "))
        print(f"Resultado: {seno(a)}")
    elif operacion == '9':
        a = float(input("Ingrese el ángulo en grados: "))
        print(f"Resultado: {coseno(a)}")
    elif operacion == '10':
        a = float(input("Ingrese el ángulo en grados: "))
        print(f"Resultado: {tangente(a)}")
    else:
        print("Operación no válida")

calculadora()