"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre
posterior a la N y el grupo B por el resto.Escribir un programa que pregunte al usuario su nombre y sexo,
y muestre por pantalla el grupo que le corresponde"""

sexo = input("Ingresa tu sexo (masculino/femenino): ").upper()
nombre = input("Ingresa tu nombre: ")
if (sexo == "femenino" and nombre[0].lower()<"m") or (sexo =="masculino" and nombre[0].lower()>"n"):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")