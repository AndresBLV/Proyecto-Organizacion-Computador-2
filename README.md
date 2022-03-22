# Proyecto-Organizacion-Computador-2

Proyecto 2 de Organización del Computador

Librería Pública de Manhattan

Escriba un programa que implemente el registro de libros de la biblioteca pública de Manhattan.
En la Base de Datos se registrará la siguiente información para cada Libro:

Cota: Código que representa cada uno de los libros registrados en la biblioteca, conformado por 6 letras y 2 dígitos (Ejemplo de un Cota: MATBYZ01). Cada libro tiene un código único.
Título: Título del libro de Máximo 30 caracteres (Ejemplo: “El Principito”). No puede haber varios libros registrados bajo el mismo título.
Serial: Código único de 12 números asignado por la editorial (ej: "000012345678")
Ejemplares Disponibles: Cantidad de ejemplares disponibles para ser prestados.
Ejemplares Prestados: Cantidad de Ejemplares que actualmente se encuentran bajo préstamo. 

Su registro de Libros debe de permitir las siguientes operaciones:

A- Inserción de un Nuevo Libro a la Base de Datos. (Se asume que todo libro se inserta con 0 ejemplares prestados)
B- Búsqueda de un Libro en la Base de Datos, Permitiendo:
  Búsqueda por Cota.
  Búsqueda por Título.
  Búsqueda por Serial.
C- Préstamo de un Libro. (Solo para aquellos que tengan Ejemplares Disponibles)
D- Retorno de un Libro. (Solo para aquellos que tengan Ejemplares Prestados)
E- Eliminación de un Libro de la Base de Datos(Físicamente)
 
Nota IMPORTANTE: Debe implementar el programa utilizando Hashing y utilizando como Clave Primaria la Cota de cada Libro. Debe prever 2 grupos primarios con capacidad de 3 libros cada uno y 6 grupos de overflow. Para buscar por Título o por Serial estos deben estar designados como Claves Secundarias. Es decir, debe construir los “‘’Índices” para realizar las búsquedas respectivas según estos Campos.

 

Plataforma: Python con vectores en memoria, pero deben poder grabarse los

resultados en disco duro al terminar el programa y leer desde disco los últimos

datos guardados cuando éste se inicia.
