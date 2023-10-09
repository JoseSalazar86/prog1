def horasTrabajo (horasTrabajadas:int,costesHoras:int):

    return horasTrabajadas * costesHoras
  
if __name__== "__main__":
 
 # Leemos los datos
 horasTrabajadas = int (input("Introduce las horas trabajadas: "))
 costesHoras = int (input("Introduce el costes por horas"))

# Procesamos los datos
 costeTotal = horasTrabajo(horasTrabajadas,costesHoras)
# Imprimos los datos
 print("El coste total es: ", costeTotal)