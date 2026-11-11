num = int(input("Ingrese el numero: "))

min1 = int(input("Ingrese el minimo del intervalo 1: "))
max1 = int(input("Ingrese el maximo del intervalo 1: "))

min2 = int(input("Ingrese el minimo del intervalo 2: "))
max2 = int(input("Ingrese el maximo del intervalo 2: "))

min3 = int(input("Ingrese el minimo del intervalo 3: "))
max3 = int(input("Ingrese el maximo del intervalo 3: "))

if (min1 < num < max1) or (min2 < num < max2) or (min3 < num < max3):
    print("El numero", num, "esta dentro de uno de los intervalos especificados")
else:
    print("El numero", num, "esta fuera de los intervalos especificados")
