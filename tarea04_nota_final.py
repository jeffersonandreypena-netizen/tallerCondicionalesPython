nota1 = float(input("Ingrese la nota del trabajo 1: "))
nota2 = float(input("Ingrese la nota del trabajo 2: "))
nota3 = float(input("Ingrese la nota del trabajo 3: "))
nota4 = float(input("Ingrese la nota del trabajo 4: "))
nota5 = float(input("Ingrese la nota del trabajo 5: "))

definitiva = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("La nota definitiva es:", definitiva)

if definitiva < 0.0 or definitiva > 5.0:
    print("Su nota es menor a 0.0 o mayor a 5.0 y es una nota inválida, por favor revise las notas insertadas")
elif definitiva > 3.5:
    print("Ganó el curso")
else:
    print("Perdió el curso")
