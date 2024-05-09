Pikachu_roll = 4500
Otaku_roll = 5000
Pulpo_venenoso_roll = 5200
Anguila_electrica_roll =4800
pedido = "x"
respuesta = False

while pedido=="x":
    print("Bienvenido a Sushi la H")
    print("Menú")
    print("1. Pikachu Roll $4500 c/u")
    print("2. Otaku Roll $5000 c/u ")
    print("3. Pulpo Venenoso Roll $5200 c/U")
    print("4. Anguila Electrica Roll $4800 c/u")
cant_pikachu =int(input("Pikachu: "))
cant_otaku =int(input("Otaku: "))
cant_pulpo =int(input("Pulpo: "))
cant_anguila =int(input("Anguila: "))

Precio_total_pedido = Pikachu_roll * cant_pikachu + Otaku_roll * cant_otaku + Pulpo_venenoso_roll * cant_pulpo + Anguila_electrica_roll * cant_anguila

nuevo_pedido =(input("¿Desea ordenar algo más?: x.si / 0.no "))
pedido=nuevo_pedido
pregunta_codigo = input("¿Posee el codigo de descuento?: 1.si/ 0.no ")

while not (respuesta):
    if pregunta_codigo =="1":
        try:
            codigo= input("Ingrese el codigo de descuento")
            if codigo =="soyotaku":
                Precio_total_pedido = (Precio_total_pedido)* 0.1
                respuesta==True
            else:
                print("Codigo ingresado no valido.")
                opcion = input("Ingrese opción (1) o vuelva al menu presionando (x)")
                pregunta_codigo = opcion
            except ValueError:
print("No se puede ingresar el texto")
opcion = input("Ingrese opción (1) o vuelva al menu presionando (x)")
pregunta_codigo = opcion
else:
print(f"El total de su pedido es: {Precio_total_pedido} ")


