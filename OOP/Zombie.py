from Enemigo import *
import random

class Zombie(Enemigo):
    def __init__(self, puntos_enemigo=10, ataque=1):
        super().__init__(tipo_enemigo='Zombie', puntos_energia=puntos_enemigo, ataque=ataque)
        
        def habla(self):
            print("*Hummmm.....*")
       
        def propagar_enfermedad(self):
            print("El zombie esta tratando de propagar la enfermedad!!")
         
         
        def ataque_especial(self):
            print("zombie ataque especial")
            funciona_ataque_especial = random.random() < 0.50
            if funciona_ataque_especial:
                self.ataque +=2
                print("zombie ha generado su energia con 2HP!!!!")
                
