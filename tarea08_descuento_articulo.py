tipo = input("Ingrese el tipo de articulo: ")
precio = float(input("Ingrese el precio del articulo: "))

if tipo == "Textil":
    print("El descuento es 0% por lo tanto su precio final es: $", precio, sep="")
elif tipo == "Electrodomestico":
    descuento = precio * 0.037
    total = precio - descuento
    print("El descuento es del 3.7%: $", descuento, sep="")
    print("El precio final es: $", total, sep="")
elif tipo == "Elementos de Cocina":
    descuento = precio * 0.042
    total = precio - descuento
    print("El descuento es del 4.2%: $", descuento, sep="")
    print("El precio final es: $", total, sep="")
elif tipo == "Videojuego":
    descuento = precio * 0.078
    total = precio - descuento
    print("El descuento es 7.8%: $", descuento, sep="")
    print("El precio final es: $", total, sep="")
else:
    print("Tipo de articulo no valido")
