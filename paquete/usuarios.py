import json

class usuario:
    def __init__(self):
        self._user = "user"
        self._password = "password"
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user (self,valor):
        self._user = valor
    
    @user.deleter
    def user(self):
        del self._user

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,valor):
        self._password = valor
    
    @password.deleter
    def usuario(self):
        del self._password
    
    def __str__(self):
        ESPACIOS = 8
        return f"""{"Usuario :":<{ESPACIOS}}{self.user}
        {"Password :":<{ESPACIOS}}{self.password}"""

class usuario_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, usuario):
            return {"Usuario":obj.user , "Password":obj.password}
        return json.JSONEncoder.default(self, obj)

def desde_json(diccionario):
        return usuario(diccionario["Usuario"],diccionario["Password"])
