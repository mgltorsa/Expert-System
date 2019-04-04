import sys

inp = input("Desea correr en modo debug? ( s/n? ): ")
print("\n")
if inp=="s":
    print("corriendo en debug_mode, podrá introducir sus propios casos\n")
    sys.argv.append("-debug")
else:
    print("corriendo sin debug \n\n")
import example