class Cine():

  def __init__(self, nombre, direccion, id=None):
    self.nombre = nombre
    self.direccion = direccion
    self.id = id
    self.programacion = []

  def get_id(self):
    return self.id

  def set_id(self, id):
    self.id = id

  def get_nombre(self):
    return self.nombre

  def get_direccion(self):
    return self.direccion

  def set_nombre(self, nombre):
    self.nombre = nombre

  def set_direccion(self, direccion):
    self.direccion = direccion

  def agregarPeliculaProgramacion(self, pelicula):
    self.programacion.append(pelicula)

  def mostrar_programacion(self):
    print(f"Programación del {self.get_nombre()}: ")
    for pelicula in self.programacion:
      print(pelicula.mostrar_info())

  def mostrar_info(self):
    return f"Cine {self.get_id()}: {self.get_nombre()}, Dirección: {self.get_direccion()}"
