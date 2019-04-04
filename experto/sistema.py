from random import choice
from pyknow import *


class Ph():
    ALCALINO = "ALCALINO"
    LIGERAMENTE_ALCALINO = "LIGERAMENTE ALCALINO"
    NEUTRO = "NEUTRO"
    LIGERAMENTE_ACIDO = "LIGERAMENTE ACIDO"
    ACIDO = "ACIDO"


class Ce():
    ALTA = "ALTA"
    BAJA = "BAJA"


class Campo(Fact):
    pass


class Experto(KnowledgeEngine):

    @Rule(Campo(ph=P(lambda ph: ph==7.2)))
    def regla_1(self):
        yield Campo(Ph.ALCALINO)
        print("> ph:%s " % (Ph.ALCALINO))

    @Rule(Campo(ph=P(lambda ph: ph > 6.8) & P(lambda ph: ph < 7.2)))
    def regla_2(self):
        yield Campo(Ph.LIGERAMENTE_ALCALINO)
        print("> ph: %s" % Ph.LIGERAMENTE_ALCALINO)

    @Rule(Campo(ph=P(lambda ph: ph <= 6.8) & P(lambda ph: ph >= 6.2)))
    def regla_3(self):
        yield Campo(Ph.NEUTRO)
        print("> ph: %s" % Ph.NEUTRO)

    @Rule(Campo(ph=P(lambda ph: ph > 5.6) & P(lambda ph: ph < 6.2)))
    def regla_4(self):
        yield Campo(Ph.LIGERAMENTE_ACIDO)
        print("> ph: %s" % Ph.LIGERAMENTE_ACIDO)

    @Rule(Campo(ph=P(lambda ph: ph <= 5.6)))
    def regla_5(self):
        yield Campo(Ph.ACIDO)
        print("> ph: %s" % Ph.ACIDO)

    @Rule(Campo(ce=P(lambda ce: ce < 0.8)))
    def regla_6(self):
        yield Campo(Ce.BAJA)
        print("> conductividadElectrica: %s " % Ce.BAJA)

    @Rule(Campo(ce=P(lambda ce: ce >= 0.8)))
    def regla_7(self):
        yield Campo(Ce.ALTA)
        print("> conductividadElectrica: %s" % Ce.ALTA)

    @Rule(Campo(Ph.ALCALINO))
    def regla_8(self):
        print("\n\n")
        print("> ExtractoSoluble: True")

    @Rule(Campo(Ph.LIGERAMENTE_ALCALINO))
    def regla_9(self):
        print("\n\n")
        print("> ExtractoSoluble: True")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
              Campo(Ph.ALCALINO),
              Campo(Ce.ALTA)))
    def regla_10(self):
        print("\n\n")
        print(">")
        print("     *-(1) Limitaciones de movimiento de agua")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     *-(4) Acumulacion de iones alcalinoterreos")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.ALCALINO),
              Campo(Ce.ALTA)))
    def regla_11(self):
        print("\n\n")
        print(">")
        print("     *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.ALCALINO),
              Campo(Ce.ALTA)))
    def regla_12(self):
        print("\n\n")
        print(">")
        print("     *-(1) Revisar las mediciones realizadas.")
        print("     *-(1) Coloraciones grises suelo (Glaizeado)")
        print("     *-(2) Suelo Hidromorfico")
        print("     *-(3) Limitaciones fisicas temporales")
        print("     *-(4) Baja difusion de Oxigeno y flujo de gases")

    @Rule(AND(Campo(arcilla=P(lambda limo: limo <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.ALCALINO),
              Campo(Ce.ALTA)))
    def regla_13(self):
        print("\n\n")
        print(">")
        print("     *-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     *-(2) Baja disponibilidad de Calcio")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
              Campo(Ph.ALCALINO),
              Campo(Ce.BAJA)))
    def regla_14(self):
        print("\n\n")
        print(">")
        print("     *-(1) Limitaciones de movimiento de agua")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     *-(4) Acumulacion de iones alcalinoterreos	")
        print("     *-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.ALCALINO),
              Campo(Ce.BAJA)))
    def regla_15(self):
        print("\n\n")
        print(">")
        print("     *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.ALCALINO),
              Campo(Ce.BAJA)))
    def regla_16(self):
        print("\n\n")
        print(">")
        print("     *-(1) Coloraciones grises suelo (Glaizeado)")
        print("     *-(2) Suelo Hidromorfico")
        print("     *-(3) Limitaciones fisicas temporales")
        print("     *-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(limo=P(lambda limo: limo <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.ALCALINO),
              Campo(Ce.ALTA)))
    def regla_17(self):
        print("\n\n")
        print(">")
        print("     *-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     *-(2) Baja disponibilidad de Calcio")
        print("     *-(3) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.LIGERAMENTE_ALCALINO)),
          Campo(Ce.ALTA))
    def regla_18(self):
        print("\n\n")
        print(">")
        print("     *-(1) Limitaciones de movimiento de agua")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     *-(4) Acumulacion de iones alcalinoterreos	")
        print("     *-(5) Alta saturación de calcio")
        print("     *-(6) Salinidad en el suelo")
        print("     *-(7) Baja disponibilidad de Fosforo (Precipitación)")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.LIGERAMENTE_ALCALINO)),
          Campo(Ce.ALTA))
    def regla_19(self):
        print("\n\n")
        print(">")
        print("     *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.LIGERAMENTE_ALCALINO)),
          Campo(Ce.ALTA))
    def regla_20(self):
        print("\n\n")
        print(">")
        print("     *-(1) Coloraciones grises suelo (Glaizeado)")
        print("     *-(2) Suelo Hidromorfico")
        print("     *-(3) Limitaciones fisicas temporales")
        print("     *-(4) Baja difusion de Oxigeno y flujo de gases")

    @Rule(AND(Campo(limo=P(lambda limo: limo <= 40.0)),
              Campo(arena=P(lambda arena: arena <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.LIGERAMENTE_ALCALINO)),
          Campo(Ce.ALTA))
    def regla_21(self):
        print("\n\n")
        print(">")
        print("     *-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     *-(2) Baja disponibilidad de Calcio")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
              Campo(Ph.LIGERAMENTE_ALCALINO)),
          Campo(Ce.BAJA))
    def regla_22(self):
        print("\n\n")
        print(">")
        print("     *-(1) Limitaciones de movimiento de agua")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     *-(4) Acumulacion de iones alcalinoterreos	")
        print("     *-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.LIGERAMENTE_ALCALINO)),
          Campo(Ce.BAJA))
    def regla_23(self):
        print("\n\n")
        print(">")
        print("     *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.LIGERAMENTE_ALCALINO)),
          Campo(Ce.BAJA))
    def regla_24(self):
        print("\n\n")
        print(">")
        print("     *-(1) Coloraciones grises suelo (Glaizeado)")
        print("     *-(2) Suelo Hidromorfico")
        print("     *-(3) Limitaciones fisicas temporales")
        print("     *-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(limo=P(lambda limo: limo <= 40.0)),
              Campo(arena=P(lambda arena: arena <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40)),
              Campo(Ph.LIGERAMENTE_ALCALINO)),
          Campo(Ce.ALTA))
    def regla_25(self):
        print("\n\n")
        print(">")
        print("     *-(1) Coloraciones grises suelo (Glaizeado)")
        print("     *-(2) Suelo Hidromorfico")
        print("     *-(3) Limitaciones fisicas temporales")
        print("     *-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
              Campo(Ph.NEUTRO),
              Campo(Ce.ALTA)))
    def regla_26(self):
        print("     *-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Salinidad en el suelo")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.NEUTRO),
              Campo(Ce.ALTA)))
    def regla_27(self):
        print("     *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.NEUTRO),
              Campo(Ce.ALTA)))
    def regla_28(self):
        print("     *-(1) Salinidad en el suelo")

    """TODO: Empezar desde la 29, hice hasta la 28, cambié nombres
        Y prints
    """

    @Rule(AND(Campo(limo=P(lambda limo: limo <= 40.0)),
              Campo(arena=P(lambda arena: arena <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.NEUTRO),
              Campo(Ce.ALTA)))
    def regla_29(self):
        print("\n\n\n")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
              Campo(Ph.NEUTRO),
              Campo(Ce.BAJA)))
    def regla_30(self):
        print("     *-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Limitaciones de movimiento de agua")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.NEUTRO),
              Campo(Ce.BAJA)))
    def regla_31(self):
        print("\n\n\n")
        print("     *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.NEUTRO),
              Campo(Ce.BAJA)))
    def regla_32(self):
        print("\n\n\n")
        print("     *-(1) Coloraciones grises suelo (Glaizeado)")

    @Rule(AND(Campo(limo=P(lambda limo: limo <= 40.0)),
              Campo(arena=P(lambda arena: arena <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.NEUTRO),
              Campo(Ce.ALTA)))
    def regla_33(self):
        print("\n\n\n")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
              Campo(Ph.LIGERAMENTE_ACIDO),
              Campo(Ce.ALTA)))
    def regla_34(self):
        print("     *-(1) Limitaciones de movimiento de agua")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     *-(4) Acumulacion de iones alcalinoterreos	")
        print("     *-(5) Alta saturación de calcio")
        print("     *-(6) Salinidad en el suelo")
        print("     *-(7) Baja disponibilidad de Fosforo (Precipitación)")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.LIGERAMENTE_ACIDO),
              Campo(Ce.ALTA)))
    def regla_35(self):
        print("\n\n\n")
        print("       *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.LIGERAMENTE_ACIDO),
              Campo(Ce.ALTA)))
    def regla_36(self):
        print("\n\n\n")

        print("     *-(1) Contenido de Aluminio")
        print("     *-(2) Sulfatos altos")
        print("     *-(3) Impedancia")

    @Rule(AND(Campo(limo=P(lambda limo: limo <= 40.0)),
              Campo(arena=P(lambda arena: arena <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.LIGERAMENTE_ACIDO),
              Campo(Ce.ALTA)))
    def regla_37(self):
        print("\n\n\n")
        print("     *-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     *-(2) Baja disponibilidad de Calcio")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
              Campo(Ph.LIGERAMENTE_ACIDO),
              Campo(Ce.BAJA)))
    def regla_38(self):
        print("     *-(1) Limitaciones de movimiento de agua")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     *-(4) Acumulacion de iones alcalinoterreos	")
        print("     *-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.LIGERAMENTE_ACIDO),
              Campo(Ce.BAJA)))
    def regla_39(self):
        print("\n\n\n")
        print("     *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.LIGERAMENTE_ACIDO),
              Campo(Ce.BAJA)))
    def regla_40(self):
        print("     *-(1) Coloraciones grises suelo (Glaizeado)")
        print("     *-(2) Suelo Hidromorfico")
        print("     *-(3) Limitaciones fisicas temporales")
        print("     *-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(limo=P(lambda limo: limo <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.LIGERAMENTE_ACIDO),
              Campo(Ce.ALTA)))
    def regla_41(self):
        print("\n\n\n")
        print("     *-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     *-(2) Baja disponibilidad de Calcio")
        print("     *-(3) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
              Campo(Ph.ACIDO),
              Campo(Ce.ALTA)))
    def regla_42(self):
        print("\n\n\n")
        print("     *-(1) Limitaciones de movimiento de agua")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Acumulacion de iones alcalinoterreos	")
        print("     *-(4) Salinidad en el suelo")
        print("     *-(5) Baja disponibilidad de Fosforo (Precipitación)")
        print("     *-(6) Baja disponibilidad de Calcio")
        print("     *-(7) Contenido de Aluminio")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.ACIDO),
              Campo(Ce.ALTA)))
    def regla_43(self):
        print("\n\n\n")
        print("     *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.ACIDO),
              Campo(Ce.ALTA)))
    def regla_44(self):
        print("\n\n\n")

        print("     *-(1) Contenido de Aluminio")
        print("     *-(2) Sulfatos altos")
        print("     *-(3) Impedancia")

    @Rule(AND(Campo(limo=P(lambda limo: limo <= 40.0)),
              Campo(arena=P(lambda arena: arena <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.ACIDO),
              Campo(Ce.ALTA)))
    def regla_45(self):
        print("\n\n\n")

        print("     *-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     *-(2) Baja disponibilidad de Calcio")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
              Campo(Ph.ACIDO),
              Campo(Ce.BAJA)))
    def regla_46(self):
        print("     *-(1) Limitaciones de movimiento de agua")
        print("     *-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     *-(4) Acumulacion de iones alcalinoterreos	")
        print("     *-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
              Campo(Ph.ACIDO),
              Campo(Ce.BAJA)))
    def regla_47(self):
        print("\n\n\n")
        print("     *-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
              Campo(Ph.ACIDO),
              Campo(Ce.BAJA)))
    def regla_48(self):
        print("\n\n\n")

        print("     *-(1) Coloraciones grises suelo (Glaizeado)")
        print("     *-(2) Suelo Hidromorfico")
        print("     *-(3) Limitaciones fisicas temporales")
        print("     *-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     *-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(limo=P(lambda limo: limo <= 40.0)),
              Campo(arena=P(lambda arena: arena <= 40.0)),
              Campo(arcilla=P(lambda arcilla: arcilla <= 40.0)),
              Campo(Ph.ACIDO),
              Campo(Ce.ALTA)))
    def regla_49(self):
        print("\n\n\n")

        print("     *-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     *-(2) Baja disponibilidad de Calcio")
        print("     *-(3) Baja disponibilidad de elementos menores ")
