""" Esto era en colab
from google.colab import drive
drive.mount('/drive/')

ruta= '/drive/MyDrive/Primer pre-entrega+Bollano """

""" Funciones """
def registro():
    Usuario = str(input("Ingrese un usuario:  "))
    Contraseña = str(input("Ingrese una contraseña:  "))
    n={"USUARIO": Usuario, "CONTRASEÑA": Contraseña}
    database= open( ruta + '/BaseDatos.txt','a')
    database.write("Usuario: "+n["USUARIO"] +" "+"Contraseña:  " +n["CONTRASEÑA"]+'\n')
    database.close()

def leerdb():
    database= open( ruta + '/BaseDatos.txt','r')
    cont=database.read()
    print(cont)
    database.close()