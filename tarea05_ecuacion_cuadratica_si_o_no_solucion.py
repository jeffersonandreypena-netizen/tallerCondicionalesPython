a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a != 0:
    discriminante = b * b - 4 * a * c
    print("La discriminante es:", discriminante)
    if discriminante >= 0:
        print("La ecuacion tiene solución")
    else:
        print("La ecuacion no tiene solución")
else:
    print("El valor de a debe ser diferente de cero")
