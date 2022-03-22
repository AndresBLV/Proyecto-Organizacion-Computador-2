class Book():
  def __init__(self,cota,titulo,serial,disponible,prestamo):
    self.__cota = cota
    self.__titulo = titulo
    self.__serial = serial
    self.__disponible = disponible
    self.__prestamo = 0

  def get_cota(self):
    return self.__cota

  def get_titulo(self):
    return self.__titulo

  def get_serial(self):
    return self.__serial

  def get_disponible(self):
    return self.__disponible

  def get_prestamo(self):
    return self.__prestamo

  def set_cota(self,new_cota):
    self.__cota = new_cota

  def set_titulo(self,new_titulo):
    self.__titulo = new_titulo

  def set_serial(self,new_serial):
    self.__serial = new_serial

  def set_disponible(self,new_disponible):
    self.__disponible = new_disponible

  def set_prestamo(self,new_prestamo):
    self.__prestamo = new_prestamo
