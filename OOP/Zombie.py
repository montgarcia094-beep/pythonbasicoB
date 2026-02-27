from Enemigo import *

class Zombie(Enemigo):
    def __init__(self, puntos_enemigo=10, ataque=1):
        super().__init__(tipo_enemigo='Zombie', punto_energia=puntos_enemigo, ataque=ataque)
        
        def habla(self):
            print("*Hummmm.....*")
        def propagar_enfermedad(self):
            print("El zombie esta tratando de propagar la enfermedad!!")
            

