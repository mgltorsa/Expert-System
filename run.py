from random import choice
from experto.sistema import *


engine = Experto()
engine.reset()


engine.declare(Campo(PH=choice([Ph.ALCALINO,Ph.LIGERAMENTE_ALCALINO,Ph.ACIDO])))
engine.declare(Campo(CE=choice([Ce.ALTA,Ce.BAJA])))
engine.declare(Campo(arcilla=choice([40.0,89.0,75])))


engine.run()