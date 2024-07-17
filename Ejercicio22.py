def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: division por cero"
    elif x ==0:
        return "Error: division por cero"
    else:
        return x / y

print("Selecciona operacion:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

while True:
    opcion = input("Ingresa opcion: 1_SUM, 2_RES, 3_MILT, 4_DIV")

    if opcion in ('1', '2', '3', '4'):
        num1 = float(input("Ingresa primer numero: "))
        num2 = float(input("Ingresa segundo numero: "))

        if opcion == '1':
            print(num1, "+", num2, "=", sumar(num1, num2))
        elif opcion == '2':
            print(num1, "-", num2, "=", restar(num1, num2))
        elif opcion == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))
        elif opcion == '4':
            print(num1, "/", num2, "=", dividir(num1, num2))
        break
    else:
        print("Opcion invalida. Intenta de nuevo.")
        