import json
""" Funciones """
database={}

""" with open(database.json,"w") as archive:
        json.dump(database, archive) """

def registro(database):
    user = input("Ingrese un usuario:  ")
    password = input("Ingrese una contraseña:  ")
    newuser = json.loads({"user": user, "password": password})
    with open(database.json,"w") as newuser:
        json.dumps(database, newuser)

def leerdb(database):
    print("La database contiene :")
    for key,value in database.items():
        print(key,":",value)

def saveArchive(database):
    ruta= r"C:\Users\Usuario\Desktop\Python\CHPython\paquete1"
    with open(ruta+r"\database.txt","w") as file:
        json.dump(database,file,indent=4)

def login(database):  
    user = input("Ingrese un usuario:  ")
    if user in database.keys():
        password = input("Ingrese su contraseña:  ")
    if database[user] == password :
        return "Sesion iniciada"
    else:
        return "Contraseña incorrecta"