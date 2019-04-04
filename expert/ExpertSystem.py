from random import choice
from pyknow import *

class Campo(Fact):
    pass

class Experto(KnowledgeEngine):

    @Rule(Campo(ph=P(lambda ph: ph == 7.2)))
    def rule_1(self):
        yield Campo(PH="ALCALINO")
        print("==> ph: ALCALINO")
        
    
    @Rule(Campo(ph=P(lambda ph: ph > 6.8) & P(lambda ph: ph < 7.2)))
    def rule_2(self):
        yield Campo(PH="LIGERAMENTE ALCALINO")
        print("==> ph: LIGERAMENTE ALCALINO")

    @Rule(Campo(ph=P(lambda ph: ph<=6.8) & P(lambda ph: ph>= 6.2)))
    def rule_3(self):
        yield Campo(PH="NEUTRO")
        print("==> ph: NEUTRO")

    @Rule(Campo(ph=P(lambda ph: ph>5.6) & P(lambda ph: ph<6.2)))
    def rule_4(self):
        yield Campo(PH="LIGERAMENTE ACIDO")
        print("==> ph: LIGERAMENTE ACIDO")

    @Rule(Campo(ph=P(lambda ph: ph <= 5.6)))
    def rule_5(self):
        yield Campo(PH="ACIDO")
        print("==> ph: ACIDO")

    @Rule(Campo(ce=P(lambda ce: ce < 0.8)))
    def rule_6(self):
        yield Campo(CE="BAJA")
        print("==> conductividadElectrica: BAJA")

    @Rule(Campo(ce=P(lambda ce: ce >= 0.8)))
    def rule_7(self):
        yield Campo(CE="ALTA")
        print("==> conductividadElectrica: ALTA")

    @Rule(Campo(PH=L("ALCALINO")))
    def rule_8(self):
        print("\n\n")
        print("==> ExtractoSoluble: True")

    @Rule(Campo(PH=L("LIGERAMENTE ALCALINO")))
    def rule_9(self):
        print("\n\n")
        print("==> ExtractoSoluble: True")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >= 40.0)),
    Campo(PH=L("ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_10(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos")

    @Rule(AND(Campo(arena=P(lambda arena: arena >= 50.0)),
    Campo(PH=L("ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_11(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >= 45.0)),
    Campo(PH=L("ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_12(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")   
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")

    @Rule(AND(Campo(arcilla=P(lambda limo: limo <= 40.0)),
    Campo(arcilla=P(lambda arcilla: arcilla <=40.0)),
    Campo(PH=L("ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_13(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >=40.0)),
    Campo(PH=L("ALCALINO")),
    Campo(CE=L("BAJA"))))
    def rule_14(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arena=P(lambda arena: arena >=50.0)),
    Campo(PH=L("ALCALINO")),
    Campo(CE=L("BAJA"))))
    def rule_15(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >=45.0)),
    Campo(PH=L("ALCALINO")),
    Campo(CE=L("BAJA"))))
    def rule_16(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(limo=P(lambda limo: limo <=40.0)),
    Campo(arcilla=P(lambda arcilla: arcilla <=40.0)),
    Campo(PH=L("ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_17(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")
    
    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla <=40.0)),
    Campo(PH=L("LIGERAMENTE ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_18(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Alta saturación de calcio")
        print("     |-(6) Salinidad en el suelo")
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)")

    @Rule(AND(Campo(arena=P(lambda arena: arena >=50.0)),
    Campo(PH=L("LIGERAMENTE ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_19(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >=45.0)),
    Campo(PH=L("LIGERAMENTE ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_20(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")

    @Rule(AND(Campo(limo=P(lambda limo: limo <=40.0)),
    Campo(arena=P(lambda arena: arena <=40.0)),
    Campo(arcilla=P(lambda arcilla: arcilla <=40.0)),
    Campo(PH=L("LIGERAMENTE ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_21(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla >=40.0)),
    Campo(PH=L("LIGERAMENTE ALCALINO")),
    Campo(CE=L("BAJA"))))
    def rule_22(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")   
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arena=P(lambda arena: arena >=50.0)),
    Campo(PH=L("LIGERAMENTE ALCALINO")),
    Campo(CE=L("BAJA"))))
    def rule_23(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo >=45.0)),
    Campo(PH=L("LIGERAMENTE ALCALINO")),
    Campo(CE=L("BAJA"))))
    def rule_24(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(limo=P(lambda limo: limo<=40.0)),
    Campo(arena=P(lambda arena: arena<=40.0)),
    Campo(arcilla=P(lambda arcilla: arcilla<=40)),
    Campo(PH=L("LIGERAMENTE ALCALINO")),
    Campo(CE=L("ALTA"))))
    def rule_25(self):
        print("\n\n")
        print("==>")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")
    
    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla>=40.0)),
    Campo(PH=L("NEUTRO")),
    Campo(CE=L("ALTA"))))
    def rule_26(self):
        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Salinidad en el suelo")
    
    @Rule(AND(Campo(arena=P(lambda arena: arena>=50.0)),
    Campo(PH=L("NEUTRO")),
    Campo(CE=L("ALTA"))))
    
    def rule_27(self):
        print("     |-(1) Revisar las mediciones realizadas.")


    @Rule(AND(Campo(limo=P(lambda limo: limo>=45.0)),
    Campo(PH=L("NEUTRO")),
    Campo(CE=L("ALTA"))))
    def rule_28(self):
        print("     |-(1) Salinidad en el suelo")
    
    @Rule(AND(Campo(limo=P(lambda limo: limo<=40.0)),
    Campo(arena=P(lambda arena: arena<=40.0)),
    Campo(arcilla=P(lambda arcilla: arcilla<=40.0)),
    Campo(PH=L("NEUTRO")),
    Campo(CE=L("ALTA"))))
    def rule_29(self):
        print("\n\n\n")
   
    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla>=40.0)),
    Campo(PH=L("NEUTRO")),
    Campo(CE=L("BAJA"))))
    def rule_30(self):
        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Limitaciones de movimiento de agua")

    @Rule(AND(Campo(arena=P(lambda arena: arena>=50.0)),
    Campo(PH=L("NEUTRO")),
    Campo(CE=L("BAJA"))))
    def rule_31(self):
        print("\n\n\n")	
        print("     |-(1) Revisar las mediciones realizadas.")


    @Rule(AND(Campo(limo=P(lambda limo: limo>=45.0)),
    Campo(PH=L("NEUTRO")),
    Campo(CE=L("BAJA"))))
    def rule_32(self):
        print("\n\n\n")	
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")

    
    
    @Rule(AND(Campo(limo=P(lambda limo: limo<=40.0)),
    Campo(arena=P(lambda arena: arena<=40.0)),
    Campo(arcilla=P(lambda arcilla: arcilla<=40.0)),
    Campo(PH=L("NEUTRO")),
    Campo(CE=L("ALTA"))))
    def rule_33(self):
        print("\n\n\n")
    

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla>=40.0)),
    Campo(PH=L("LIGERAMENTE ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_34(self):
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")    
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Alta saturación de calcio")
        print("     |-(6) Salinidad en el suelo")
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)")
            

    @Rule(AND(Campo(arena=P(lambda arena: arena>=50.0)),
    Campo(PH=L("LIGERAMENTE ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_35(self):
        print("\n\n\n")
        print("       |-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo>=45.0)),
    Campo(PH=L("LIGERAMENTE ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_36(self):
        print("\n\n\n")

        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")

    @Rule(AND(Campo(limo=P(lambda limo: limo<=40.0)),
    Campo(arena=P(lambda arena: arena<=40.0)),
    Campo(arcilla=P(lambda arcilla: arcilla<=40.0)),
    Campo(PH=L("LIGERAMENTE ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_37(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")  

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla>=40.0)),
    Campo(PH=L("LIGERAMENTE ACIDO")),
    Campo(CE=L("BAJA"))))
    def rule_38(self):
          print("     |-(1) Limitaciones de movimiento de agua")
          print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
          print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
          print("     |-(4) Acumulacion de iones alcalinoterreos	")
          print("     |-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arena=P(lambda arena: arena>=50.0)),
    Campo(PH=L("LIGERAMENTE ACIDO")),
    Campo(CE=L("BAJA"))))
    def rule_39(self):
        print("\n\n\n")	
        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo:limo>=45.0)),
    Campo(PH=L("LIGERAMENTE ACIDO")),
    Campo(CE=L("BAJA"))))
    def rule_40(self):
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")    
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(limo=P(lambda limo:limo<=40.0)),
    Campo(arcilla=P(lambda arcilla:arcilla<=40.0)),
    Campo(PH=L("LIGERAMENTE ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_41(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla>=40.0)),
    Campo(PH=L("ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_42(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Acumulacion de iones alcalinoterreos	")
        print("     |-(4) Salinidad en el suelo")
        print("     |-(5) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(6) Baja disponibilidad de Calcio")
        print("     |-(7) Contenido de Aluminio")


    @Rule(AND(Campo(arena=P(lambda arena: arena>=50.0)),
    Campo(PH=L("ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_43(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo>=45.0)),
    Campo(PH=L("ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_44(self):
        print("\n\n\n")
		
        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")


    @Rule(AND(Campo(limo=P(lambda limo: limo<= 40.0)),
    Campo(arena=P(lambda arena: arena<=40.0)),
    Campo(arcilla=P(lambda arcilla: arcilla<=40.0)),
    Campo(PH=L("ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_45(self):
        print("\n\n\n")
		
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")

    @Rule(AND(Campo(arcilla=P(lambda arcilla: arcilla>=40.0)),
    Campo(PH=L("ACIDO")),
    Campo(CE=L("BAJA"))))
    def rule_46(self):
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")    
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")
    @Rule(AND(Campo(arena=P(lambda arena: arena>=50.0)),
    Campo(PH=L("ACIDO")),
    Campo(CE=L("BAJA"))))
    def rule_47(self):
        print("\n\n\n")	
        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(AND(Campo(limo=P(lambda limo: limo>=45.0)),
    Campo(PH=L("ACIDO")),
    Campo(CE=L("BAJA"))))
    def rule_48(self):
        print("\n\n\n")
		
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")
    
    @Rule(AND(Campo(limo=P(lambda limo: limo<= 40.0)),
    Campo(arena=P(lambda arena: arena<=40.0)),
    Campo(arcilla=P(lambda arcilla: arcilla<=40.0)),
    Campo(PH=L("ACIDO")),
    Campo(CE=L("ALTA"))))
    def rule_49(self):
        print("\n\n\n")
		
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")   
        print("     |-(3) Baja disponibilidad de elementos menores ") 




