base_de_datos={
    "hola":"Hola, gusto en saludarte",
    "como estas?":"Bien y tu?",
    "que es python?":"Python es un lenguaje de programación"
    }
while True:
 mensaje=input("Escribe un mensaje").lower()
 if mensaje in base_de_datos: 
  print("Bot: ", base_de_datos[mensaje]) 
 elif "adios" in mensaje: 
  print("adios, que tengas un buendia ;)")
 elif "salir" in mensaje:
   print("Fue un gusto hablar contigo...saliendo del chat")
   break
 else: 
  print("No comprendo ese mensaje soy un poco retrasado XD")