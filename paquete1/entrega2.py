class Cliente:
    def __init__(self, cliente, contacto, email, saldo, intereses):
        self.cliente = cliente
        self.contacto = contacto
        self.email = email
        self.saldo = saldo
        self.intereses= intereses

    def __str__(self) :
        print("Se creo correctamente un nuevo cliente...")
        return "El nuevo cliente es: "+str(self.cliente)

    def cargar_saldo(self):
        self.saldo= input("Ingrese cuando quiere cargar: ")
        saldo += self.saldo;
        print(f"El saldo es {self.saldo}")

    def comprar(self):
        compra = input("Ingrese la compra: ")
        costo = input("Ingrese el costo: ")
        self.saldo = self.saldo - costo;