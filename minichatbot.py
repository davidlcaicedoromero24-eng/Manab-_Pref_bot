
while True:
 mensaje=input("Escribe un mensaje").lower()
 if "hola" in mensaje: 
  print("Hola, gusto en saludarte :)")
 elif "adios" in mensaje: 
  print("adios, que tengas un buendia ;)")
 elif "salir" in mensaje:
   print("Fue un gusto hablar contigo...saliendo del chat")
   break
 else: 
  print("No comprendo ese mensaje soy un poco retrasado XD")