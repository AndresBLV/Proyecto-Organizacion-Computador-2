from funciones import *

def main():
  db = {'libros':{},'cota':[],'titulo':[],'serial':[],'disponible':0,'prestamo':0}
  hash_table = [
                  [[],    [],[],[],[],[],[] ],

                  [[],    [],[],[],[],[],[] ]
                ]
  db = recive_data_text('base.txt',db)
  
  while True:
    print("Bienvendos al registro de libros de la Librería Pública de Manhattan")
    print("\n")
    print("Que operacion desea realizar:")
    print("\n")

    while True:
      try:
        option = int(input("Ingrese la opcion que desea realizar:\n1.-Insercion de un nuevo libro\n2.-Buscar un libro\n3.-Prestar un libro\n4.-Retornar un libro\n5.-Eliminar un libro\n6.-Salir\n==> "))
        if option not in range(1,7):
          raise Exception
        break
      except:
        print('Ingreso un valor invalido')
        print('\n')

    if option == 1:
      print('\n')
      db = book_register(db,hash_table)
      load_data_txt('base.txt',db)
      print('\n')
    elif option == 2:
      print('\n')
      search_menu(hash_table)
      load_data_txt('base.txt',db)
      print('\n')
    elif option == 3:
      print('\n')
      db = book_loan(db)
      load_data_txt('base.txt',db)
      print('\n')
    elif option == 4:
      print('\n')
      db = book_return(db)
      load_data_txt('base.txt',db)
      print('\n')
    elif  option == 5:
      print('\n')
      db = book_delete(db)
      load_data_txt('base.txt',db)
      print('\n')
    else:
      print('Gracias por su vistia')
      print('Vuelva pronto')
      break
      
main()