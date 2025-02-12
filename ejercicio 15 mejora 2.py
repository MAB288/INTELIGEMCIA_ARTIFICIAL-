import random
import datetime

tienda = input("Tienda: ")
folio = random.randint(1, 100)
fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cliente = input("Cliente: ")
producto = input("Producto: ")
total_compra = float(input("Ingresa el total de tu compra: "))


descuento = 0
total_final = total_compra

if total_compra > 100:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento

print("\n=================== TICKET DE COMPRA =============")
print(f"Tienda: {tienda}")
print(f"Folio: {folio}")
print(f"Fecha y Hora: {fecha_hora}")
print("-----------------------------------------")
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Total de la compra: ${total_compra:.2f}")

if descuento > 0:
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total a pagar con descuento: ${total_final:.2f}")
else:
    print("No se aplicó descuento.")

print("---------------------------------------------------------------")
print("¡Gracias por tu compra! ¡Vuelve pronto!")
print("=================================================================")