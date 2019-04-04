from random import choice
from experto.sistema import *


engine = Experto()
engine.reset()

engine.declare(Campo(ph=7.2))

engine.run()