import random




letters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"



length = int(input("¿Qué tan larga quieres tu contraseña?"))
result = ""
for i in range(length):

    result += random.choice(letters)


print(f"Tu contraseña es: {result}")

 