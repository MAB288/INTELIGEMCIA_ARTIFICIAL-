nombre = input("ingresa el nombre: ")

producto = input("ingresa el nombre del producto: ")

total_compra = float(input("ingresa el total de tu compra: "))
if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra-descuento
    print(f"¡felisidades! tienes un descuento del 10%. el total a pagar es: {total_final}")
else:

    print(f" el total a pagar es: {total_compra}")