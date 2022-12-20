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

    def cargar_saldo(self,cargar):
        nuevo_saldo =self.saldo + cargar;
        self.saldo = nuevo_saldo;
        print(f"Se cargo a su cuenta: ",cargar)
        print(f"El saldo es ",nuevo_saldo)

    def comprar(self, compra, costo):
        if self.saldo >= int(costo) :
            self.saldo -= int(costo);
            print(f"El cliente ",self.cliente," realizo la compra de ",compra," la cual costo ",costo)
            print(f"El saldo restante es ",self.saldo)
        else:
            print(f"El cliente no cuenta con el saldo")