import json
from usuarios import *
import os
import pathlib

class Inicio:
    registro = 1
    guardarUsuarios = 2
    leerdb = 3
    login = 4
    salir = 0
    
    def __init__(self):
        self._usuarios = []
        self.leerdb("usuarios.json")

    def __del__(self):
        pass

    @property
    def usuarios(self):
        return self._usuarios
    
    @usuarios.setter
    def usuarios(self,valor):
        self._usuarios = valor
    
    @usuarios.deleter
    def usuarios(self):
        del self._usuarios

def leerdb(self,ruta):
    if pathlib.Path(ruta).exists():
        with open(ruta, "r") as archive:
            data = json.load(archive)
        for us in data["usuarios"]:
            self._usuarios.append(desde_json(us))

def guardarUsuarios(self,ruta):
    with open(ruta, "w") as archive:
            json.dump({"usuarios":self.usuarios}, archive, cls=usuario_encoder, indent=4)

def registro(self):
    os.system("clc")
    print("  Registro  ")
    user = input("Ingrese un usuario:  ")
    password = input("Ingrese una contraseña:  ")
    self.usuarios.append(usuario(user,password))

def login(self):  
    os.system("cls")
    print("  Login  ")
    user = input("Ingrese un usuario:  ")
    password = input("Ingrese una contraseña:  ")
    if len(self.usuario) != 0 :
        intentos = 0
        while intentos <= 3 :
            for us in self.usuarios:
                if (f"{us[password]}") == password :
                    print("Ingreso correcto")

                    break

                else:
                    return("Contraseña incorrecta")
                    intentos += 1;
        return ("Supero el limite de intentos")
    else:
        return("Usuario incorrecto")

def menu(self):
    continuar = True
    while continuar :
        os.system("cls")
        print(f'''              INICIO
        {Inicio.registro}) Registrarse
        {Inicio.guardarUsuarios}) Guardar el nuevo usuario
        {Inicio.leerdb}) Leer base de datos
        {Inicio.login}) Login
        {Inicio.salir}) Salir
        ''')
        opc=input("Ingrese una opcion")
        try:
            opc= int(opc)
        except:
            opc=-1
        if opc == Inicio.registro :
            self.registo()
        elif opc == Inicio.guardarUsuarios :
            self.guardarUsuarios()
        elif opc == Inicio.leerdb :
            self.leerdb()
        elif opc == Inicio.login :
            self.login()
        elif opc == Inicio.salir :
            continuar = False
        else:
            os.system("cls")
            print("Opcion incorrecta")
        input("Presione enter para continuar")
    input("Presione enter para salir")