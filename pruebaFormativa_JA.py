PikachuRoll = 4500
OtakuRoll = 5000
PulpoVenenoso = 5200
AnguilaElectrica =4800

print("Bienvenido a Sushi la H")

print("Menú")

print("1. Pikachu Roll $4500 c/u")
print("2. Otaku Roll $5000 c/u ")
print("3. Pulpo Venenoso Roll $5200 c/U")
print("4. Anguila Electrica Roll $4800 c/u")
print("5. Terminar pedido")

while True:

opcion = input("Por favor, seleccione una opción (1-5):")

if opcion == "1":
    print("Has seleccionado Pikachu Roll $4500  ")
elif opcion == "2":
    print("Has seleccionado Otaku Roll $5000 ")
elif opcion == "3":
    print("Has seleccionado la opción 3 ")
elif opcion == "4":
    print("Has seleccionado la opción 4 ")
elif opcion == "5":
    print("Has seleccionado la opcion 5 ")
else:
    print("Opción invalida. Por favor, seleccione una opción valida.")