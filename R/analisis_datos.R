# Cargar los datos económicos generados en Python
datos <- read.csv("../data/datos_economicos.csv")
#Mostrar datos
print(datos)
# Crear un vector con tres departamentos
departamentos_2 <- c("Lima", "Arequipa", "Cusco")
# Mostrar el vector
print(departamentos_2)
# Crear una matriz con los ingresos promedio mensuales
ingresos_mesuales <- matrix(datos$Ingreso[1:3],nrow = 3,ncol = 1)
# Mostrar la matriz
print(ingresos_mesuales)
# Crear un data frame con las demás variables
datos_2 <- data.frame(Poblacion = datos$Poblacion[1:3],Numero_hogares = datos$Numero_hogares[1:3],Actividad_principal = datos$Actividad_principal[1:3])
# Mostrar el data frame
print(datos_2)
# Mostrar la estructura del vector de departamentos
str(departamentos_2)
# Mostrar la estructura de la matriz de ingresos
str(ingresos_mesuales)
# Mostrar la estructura del data frame
str(datos_2)