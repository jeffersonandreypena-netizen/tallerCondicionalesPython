num = float(input("Digite un número "))

# Nota: el segundo rango (>= 9.3 y < 4.5) es imposible, igual que en el original de PSeInt.
if (num > 3.5 and num <= 7.8) or (num >= 9.3 and num < 4.5) or (num >= 23.4 and num <= 45.3):
    print("El número está dentro del rango")
else:
    print("El número fuera del rango")
