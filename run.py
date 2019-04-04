from random import choice
from experto.sistema import *
import sys

debug_mode = False


class Test():
    def __init__(self, number):
        self.number = number

    def set_ph(self, campo):
        self.campo = campo


test_cases = []


def activate_debug_mode(args):
    for arg in args:
        if(arg == "-debug"):
            debug_mode = True



if debug_mode:
    print("Iniciando caso")
    finish = False
    while not finish:
        inp = input("Los atributos validos son ph, ce, arena, arcilla, limo\n"+
            "Ingrese datos de la forma attributo : atributo = valor. Nota: presione e para salir")
        if inp == "z":
            finish=True
        else:
            
        

        

    
    


else:
    engine = Experto()
    engine.reset()

    engine.declare(
        Campo(choice([Ph.ALCALINO, Ph.LIGERAMENTE_ALCALINO, Ph.ACIDO])))
    engine.declare(Campo(choice([Ce.ALTA, Ce.BAJA])))
    engine.declare(Campo(ph=choice([7.2])))


engine.run()
