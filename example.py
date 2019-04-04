from random import choice
from experto.sistema import *
import sys

debug_mode = False

for arg in sys.argv:
    if arg == "-debug":
        debug_mode = True

engine = Experto()
engine.reset()


if debug_mode:
    print("Iniciando caso")
    finish = False
    campos = []
    while not finish:
        inp = input("Los atributos validos son ph, ce, arena, arcilla, limo\n" +
                    "Ingrese datos de la forma attributo : atributo=valor.\n" +
                    "Los valores solo podran ser numeros reales\n" +   
                    "Nota: presione e para salir y s para correr el test.\n ")
        if inp == "e":
            finish = True
            print("saliendo\n")
        elif inp == "s":
            print("Corriendo test \n")            
            engine.reset()
            for campo in campos:
                engine.declare(campo)
            engine.run()
            campos = []
            print("finalizando test \n")
        else:
            
            info = inp.split("=")
            if info[0] == "ph":
                campos.append(Campo(ph=float(info[1])))
            elif info[0] == "ce":
                campos.append(Campo(ce=float(info[1])))
            elif info[0] == "arena":
                campos.append(Campo(arena=float(info[1])))
            elif info[0] == "arcilla":
                campos.append(Campo(arcilla=float(info[1])))
            elif info[0] == "limo":
                campos.append(Campo(limo=float(info[1])))
            else:
                print("no es un atributo valido\n")
                continue
            print("atributo asignado\n")


else:
    
    print("Corriendo test default, use '-debug' como parametro para correr este script\n"+
         "para ingresar datos personalizados\n")
    engine.declare(
        Campo(choice([Ph.ALCALINO, Ph.LIGERAMENTE_ALCALINO, Ph.ACIDO])))
    engine.declare(Campo(choice([Ce.ALTA, Ce.BAJA])))
    engine.declare(Campo(ph=choice([7.2])))
    engine.run()
