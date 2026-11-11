precio = float(input("Ingrese el precio del articulo "))

if precio > 150000:
    descuento = precio * 0.05
else:
    descuento = 0

total = precio - descuento

print("El descuento es:", descuento)
print("El precio final es:", total)
