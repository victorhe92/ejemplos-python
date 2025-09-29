# Programa que demuestra el uso de condiciones múltiples con if, elif y else usando el operador and solo con condiciones numéricas

edad = int(input("Introduce tu edad: "))

if edad >= 18 and edad <= 65:
  print("Eres un adulto en edad laboral.")
elif edad > 65 and edad <= 100:
  print("Eres un adulto mayor.")
elif edad >= 0 and edad < 18:
  print("Eres menor de edad.")
else:
  print("Edad no válida.")