num1 = float(input("Digite el primer número "))
num2 = float(input("Digite el segundo número "))
num3 = float(input("Digite el tercer número "))
num4 = float(input("Digite el cuarto número "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print("El número", num1, "es el mayor")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("El número", num2, "es el mayor")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("El número", num3, "es el mayor")
else:
    print("El número", num4, "es el mayor")
