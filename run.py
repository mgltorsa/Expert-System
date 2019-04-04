from expert.ExpertSystem import Experto

engine = Experto()

engine = Experto()
engine.reset()
engine.declare(Campo(PH=choice(["ALCALINO"])))
engine.declare(Campo(CE=choice(["ALTA"])))
engine.declare(Campo(arcilla=choice([40.0])))
engine.run()