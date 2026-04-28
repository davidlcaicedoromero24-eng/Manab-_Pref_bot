Nombre=input("Cual es tu nombre?")
Apellido=input("Cual es tu apellido?")
Edad=int (input("Cual es tu edad?"))
print(f"Hola, Bienvenido {Nombre} {Apellido}")
if Edad>=18:
 print(f"{Nombre} eres mayor de edad")
else:
  print(f"{Nombre} ERES MENOR DE EDAD, SAL DE AQUI")