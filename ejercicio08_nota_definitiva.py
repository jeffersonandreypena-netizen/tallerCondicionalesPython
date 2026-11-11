nota = float(input("Digita la nota "))

if nota < 0 or nota > 5:
    print("Su nota es inválida")
elif nota < 3.0:
    print("Insuficiente")
elif nota <= 3.5:
    print("Aceptable")
elif nota <= 4.0:
    print("Sobresaliente")
else:
    print("Excelente")
