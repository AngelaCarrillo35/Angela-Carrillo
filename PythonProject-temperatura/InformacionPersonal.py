#Diccionario información fisica de una persona
información_personal = {"nombre": "Lourdes", "edad": 24, "ciudad": "Quito", "telefono": 593983416514,
 "profesion": "Licenciada"}
información_personal["ciudad"]= "Ambato" # "ciudad" se modifico con una ciudad diferente.
información_personal["profesión"]= "Ingeniera" #nueva clave-valor que representa la "profesion" de la persona.
del(información_personal["edad"]) #Elimina la clave "edad".
print(información_personal)
