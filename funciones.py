from book import Book

def book_register(db):
  while True:
    try:
      cota = input('Ingrese la cota del libro a registrar:\n=> ').upper()
      if len(cota) != 8 or cota in db['cota'] or valid(cota):
        raise Exception
      break
    except:
      print('Ingreso una cota invalida, recuerde que debe contener 6 letras y 2 digitos')

  while True:
    try:
      serial = input('Ingrese el serial asignado por la editorial:\n=> ')
      if len(serial) != 12 or serial in db['serial'] or not (serial.isnumeric()):
        raise Exception
      break
    except:
      print('El codigo debe ser numerico y de 12 caracteres')

  while True:
    try:
      titulo = input('Ingrese el titulo del libro:\n=> ').title()
      if len(titulo) > 30 or titulo in db['titulo']:
        raise Exception
      break
    except:
      print('El titulo ingresa ya existe o no cumple los estandares necesarios')

  while True:
    try:
      disponibilidad = int(input('Ingrese la disponibilidad del libro ingresado:\n=> '))
      break
    except:
      print('Ingresa un valor valido')

  book = Book(cota,titulo,serial,disponibilidad,0)

  db['libros'][serial] = book
  db['cota'].append(cota)
  db['titulo'].append(titulo)
  db['serial'].append(serial)
  db['disponible'] += disponibilidad

  print('El libro ha sido registrado')
  return db
  
def valid(cota):
  count = 0
  for char in cota:
    if char.isdigit():
      count +=1
  if count == 2:
    return False
  else:
    return True

def book_loan(db):
  print('Ejemplares disponibles')
  if db['disponible'] == 0:
    print('No hay ejemplares disponibles en la libreria')
    return db
  for i,(key,value) in enumerate(db['libros'].items()):
    if value.get_disponible() != 0:
      print(f'{i+1}.-Titulo: {value.get_titulo()}; disponibilidad: {value.get_disponible()}')
  while True:
    try:
      selecction = int(input('Ingrese el indice del ejemplear deseado:\n=> '))
      if (selecction-1) not in range(0,len(db['libros'])):
        raise Exception
      break
    except:
      print('Ingresa una opcion valida')

  for i,libro in enumerate(db['libros']):
    if (selecction-1) == i:
      disponible = db['libros'][libro].get_disponible() - 1
      prestamo = db['libros'][libro].get_prestamo() + 1
      db['libros'][libro].set_disponible(disponible)
      db['libros'][libro].set_prestamo(prestamo)
      db['disponible'] -= 1
      db['prestamo'] += 1

  print('\n')
  print('Se ha realizado el prestamo del libro seleccionado')
  
  return db

def book_return(db):
  print(f'Ejemplares prestados')
  if db['prestamo'] == 0:
    print('No hay ejemplares prestados en la libreria')
    return db
  for i,(key,value) in enumerate(db['libros'].items()):
    if value.get_prestamo() != 0:
      print(f'{i+1}.-Titulo: {value.get_titulo()}; prestados: {value.get_prestamo()}')
  
  while True:
    try:
      selecction = int(input('Ingrese el indice del ejemplear a regresar:\n=> '))
      if (selecction-1) not in range(0,len(db['libros'])):
        raise Exception
      break
    except:
      print('Ingresa una opcion valida')
      
  for i,libro in enumerate(db['libros']):
    if (selecction-1) == i:
      disponible = db['libros'][libro].get_disponible() + 1
      prestamo = db['libros'][libro].get_prestamo() - 1
      db['libros'][libro].set_disponible(disponible)
      db['libros'][libro].set_prestamo(prestamo)
      db['disponible'] += 1
      db['prestamo'] -= 1

  print('\n')
  print('Se ha retornado el libro seleccionado')
  
  return db

  def recive_data_text(name_txt,db):
  """
  Parametro: La funcion recibe por parametro el diccionario db(dict) y un archivo.txt.
  Return: La funcion retorna el diccionario con los datos serializados en el archivo.txt.
  """

  binary_read = open(name_txt,'rb') # Se abre el archivo 

  if os.stat(name_txt).st_size != 0: # Se comprueba que no este vacio
    db = pickle.load(binary_read) # Si no esta vacio se extraen los datos en el diccionario

  binary_read.close() # Se cierra el archivo

  return db

def load_data_txt(name_txt,db):
  """
  Parametro: La funcion recibe por parametro el archivo de texto y el diccionario db(dict).
  Return: La funcion no retorna ningun valor, se encarga de serializar los datos contenidos en el diccionario en el archivo de texto.
  """
  # Se abre el archivo para hacer la escritura binaria
  binary_write = open(name_txt,'wb')

  db = pickle.dump(db,binary_write) #Se extraen los daos del diccionarioy se guardan en el txt

  binary_write.close() # Se cierra el archivo