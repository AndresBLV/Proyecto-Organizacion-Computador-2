
def main():
  db = {'cota':{},'titulo':(),'serial':(),'disponible':(),'prestamo':()}

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
      break
    elif option == 2:
      break
    elif option == 3:
      break

    elif option == 4:
      break

    elif  option == 5:
      break 
    else:
      print('Gracias por su vistia')
      print('Vuelva pronto')
      break
      
main()