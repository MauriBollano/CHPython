from paquete.entrega2 import Cliente
from paquete.entrega1 import Inicio

""" 
Esto es para entrega 1: Modifique el codigo para realizar el registro, login y lectura de la base de datos con diccionarios y objetos pero aun no anda

"""  
"""
def main():
    us = Inicio()
    us.menu()

if __name__ == '__main__':
    main()
"""  


""" 
Esto es para entrega 2: Crea un objeto cliente con los atributos: 
- Nombre
- N Telefono
- Email
- Saldo a favor
- Gustos/Intereses

Los metodos de cliente son:

- cargar_saldo(Carga saldo a la cuenta del cliente)
- comprar ( verifica el saldo dispoible e imprime la compra, el costo y el saldo restante si este es suficiente)

"""
cliente1 = Cliente("mauricio", 45678, "mb@gmail.com", 1000, ["moda","computacion"]) 

""" print(cliente1)

print("el saldo es: ",cliente1.saldo)

cliente1.cargar_saldo(500) 
"""
""" print("el saldo es: ",cliente1.saldo)

cliente1.comprar("computadora","800") """