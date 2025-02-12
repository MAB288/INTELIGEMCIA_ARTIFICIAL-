import datetime 
nombre = input("ingresa tu nombra: ")

fecha = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
print(f"nombre del cliente: {nombre} y la fecha y hora : {fecha}")