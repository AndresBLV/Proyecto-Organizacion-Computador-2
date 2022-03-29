from book import Book
import pickle
import os
def search_menu(hash_table):
  while True:
      try:
        option = int(input("Ingrese la opcion que desea realizar:\n1.-Busqueda por Cota\n2.-Busqueda por Titulo\n3.-Busqueda por Serial\n4.-Volver al Menu Principal\n==> "))
        if option not in range(1,5):
          raise Exception
      except:
        print('Ingreso un valor invalido')
        print('\n')
      
      if option == 1:
        while True:
          try:
            cota = input('Ingrese la cota del libro a buscar:\n=> ')
            if (valid(cota) != True):
              raise Exception
            posicion = hash(cota)
            encontrado = False
            for estanteria in hash_table[posicion]:
              for estante in estanteria:
                if cota == estante.get_cota():
                  encontrado = True
                  libro = estante
                  break
            if encontrado == False:
              print(f"La cota '{cota}' no corresponde a ningun libro registrado")
            else:
              print(f"Cota: {libro.get_cota()}\nTitulo: {libro.get_titulo()}\nSerial: {libro.get_serial()}\nDisponibles:{libro.get_disponible()}\nPrestados:{libro.get_prestamo()}")
            break
          except:
            print('Ingreso una cota invalida, recuerde que debe contener 6 letras y 2 digitos')
             
      elif option == 2:
        while True:
          try:
            titulo = input('Ingrese el titulo del libro a buscar:\n=> ').title()
            if (len(titulo) > 30) :
              raise Exception
            posicion = hash(titulo)
            encontrado = False
            for estanteria in hash_table[posicion]:
              for estante in estanteria:
                if cota == estante.get_titulo():
                  encontrado = True
                  libro = estante
                  break
            if encontrado == False:
              print(f"El titulo '{titulo}' no corresponde a ningun libro registrado")
            else:
              print(f"Cota: {libro.get_cota()}\nTitulo: {libro.get_titulo()}\nSerial: {libro.get_serial()}\nDisponibles:{libro.get_disponible()}\nPrestados:{libro.get_prestamo()}")
            break
          except:
            print('Ingreso un titulo invalido recuerde que como maximo son 30 caracteres')
      elif option == 3:
        while True:
          try:
            serial = input('Ingrese el serial del libro a buscar:\n=> ')
            if(len(serial) != 12) or not (serial.isnumeric()):
              raise Exception
            posicion = hash(serial)
            encontrado = False
            for estanteria in hash_table[posicion]:
              for estante in estanteria:
                if serial == estantes.get_serial():
                  encontrado = True
                  libro = estante
                  break
            if encontrado == False:
              print(f"El serial '{serial}' no corresponde a ningun libro registrado")
            else:
              print(f"Cota: {libro.get_cota()}\nTitulo: {libro.get_titulo()}\nSerial: {libro.get_serial()}\nDisponibles:{libro.get_disponible()}\nPrestados:{libro.get_prestamo()}")
            break
          except:
            print('Ingreso un serial invalido, recuerde que debe ser minimo 12 caracateres numericos')
      else:
        break

def book_register(db,hash_table):
  while True:
    try:
      cota = input('Ingrese la cota del libro a registrar:\n=> ')
      if (cota in db['cota']) or (valid(cota) != True):
        raise Exception
      break
    except:
      print('Ingreso una cota invalida, recuerde que debe contener 6 letras y 2 digitos')

  while True:
    try:
      serial = input('Ingrese el serial asignado por la editorial:\n=> ')
      if (len(serial) != 12) or (serial in db['serial']) or not (serial.isnumeric()):
        raise Exception
      break
    except:
      print('El codigo debe ser numerico y de 12 caracteres')

  while True:
    try:
      titulo = input('Ingrese el titulo del libro:\n=> ').title()
      if (len(titulo) > 30) or (titulo in db['titulo']):
        raise Exception
      break
    except:
      print('El titulo ingresa ya existe o no cumple los estandares necesarios')

  while True:
    try:
      disponibilidad = int(input('Ingrese la disponibilidad del libro ingresado:\n=> '))
      if (disponibilidad < 1):
        raise Exception
      break
    except:
      print('Ingresa un valor valido')

  book = Book(cota,titulo,serial,disponibilidad,0)

  db['libros'][cota] = book
  db['cota'].append(cota)
  db['titulo'].append(titulo)
  db['serial'].append(serial)
  db['disponible'] += disponibilidad

  posicion = hash(cota)
  for estanteria in hash_table[posicion]:
    if len(estanteria) < 3:
      estanteria.append(book)
      
      break 
      
  print('El libro ha sido registrado')
  return db, hash_table
  
def valid(cota):
  
  letterCount = 0
  numberCount = 0
  counter = 0
  isValid = False
  if len(cota) != 8:
    return isValid
  else:
    for x in cota:
      if x.isalpha():
        letterCount += 1
      if (counter == 6 and int(x.isnumeric())) or (counter == 7 and int(x.isnumeric())):
        numberCount += 1
      counter += 1
    if letterCount == 6 and numberCount == 2:
      isValid = True
      return isValid
    else:
      return isValid  

def hash(cota):
  valor = 0
  posicion = 1
  for x in cota:
    
    if ord(x) >= 48 and ord(x) <=57:
        valor += ((ord(x)-47)*posicion)
    
    elif ord(x)>=65 and ord(x) <=90:
        valor += ((ord(x)-54)*posicion)
    
    elif ord(x) >=97 and ord(x) <=122:
        valor += ((ord(x) - 60)*posicion)
    
    posicion += 1 
  
  return (valor % 2)

def book_loan(db,hash_table):
  print('Ejemplares disponibles')
  if db['disponible'] == 0:
    print('No hay ejemplares disponibles en la libreria')
    return db
  for i,(key,value) in enumerate(db['libros'].items()):
    if value.get_disponible() != 0:
      print(f'{i+1}.-Cota: {value.get_cota()}; Titulo: {value.get_titulo()}; disponibilidad: {value.get_disponible()}')
  while True:
    try:
      cota = input('Ingrese la cota del libro a buscar:\n=> ')
      if (valid(cota) != True):
        raise Exception
    except:
      print('Cota invalida')
   
    for key,libro in (db['libros'].items()):
      if (cota) == key:
        disponible = libro.get_disponible() - 1
        prestamo = libro.get_prestamo() + 1
        libro.set_disponible(disponible)
        libro.set_prestamo(prestamo)
        db['disponible'] -= 1
        db['prestamo'] += 1

        print('\n')
        print('Se ha realizado el prestamo del libro seleccionado')
        
        return db,hash_table
                    
def book_return(db,hash_table):
  print(f'Ejemplares prestados')
  if db['prestamo'] == 0:
    print('No hay ejemplares prestados en la libreria')
    return db
  for i,(key,value) in enumerate(db['libros'].items()):
    if value.get_prestamo() != 0:
      print(f'{i+1}.-Cota: {value.get_cota()}; Titulo: {value.get_titulo()}; prestados: {value.get_prestamo()}')
  
  while True:
    try:
      cota = input('Ingrese la cota del libro a regresar:\n=> ')
      if (valid(cota) != True):
        raise Exception
    except:
      print('Cota invalida')
    
    for key,libros in (db['libros'].items()):
      if (cota) == key:
        disponible = libros.get_disponible() - 1
        prestamo = libros.get_prestamo() + 1
        libros.set_disponible(disponible)
        libros.set_prestamo(prestamo)
        db['disponible'] += 1
        db['prestamo'] -= 1

        print('\n')
        print('Se ha realizado el prestamo del libro seleccionado')
        
        return db,hash_table
                    

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

def book_delete(db):
  if len(db['libros']) == 0:
    print('No hay libros registrados en la libreria')
    return db
    
  while True:
    try:
      serial = input('Ingrese el serial del libro que desea eliminar:\n=> ')
      if len(serial) != 12 or not (serial.isnumeric()):
        raise Exception
      break
    except:
      print('El codigo debe ser numerico y de 12 caracteres')

  for key,values in db['libros'].items():
    if key == serial:
      cota = values.get_cota()
      titulo = values.get_titulo()
      disponible = values.get_disponible()
      prestamo = values.get_prestamo()

      del db['libros'][serial]
      db['cota'].remove(cota)
      db['titulo'].remove(titulo)
      db['disponible'] -= disponible
      db['prestamo'] -= prestamo

      print('Libro eliminado con exito')
      return db

  print('El libro que desea eliminar no se encuentra registrado')
  
  return db
  