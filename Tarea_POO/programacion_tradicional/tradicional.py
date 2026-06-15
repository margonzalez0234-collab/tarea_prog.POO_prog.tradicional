def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie: ")
    edad = int(input("Ingrese la edad: "))
    return nombre, especie, edad

def mostrar_informacion(nombre, especie, edad):
    print("\n--- INFORMACION DE LA MASCOTA---")
    print("Nombre: ", nombre)
    print("Especie: ", especie)
    print("Edad: ", edad, "años")

nombre, especie, edad = registrar_mascota()
mostrar_informacion(nombre, especie, edad)