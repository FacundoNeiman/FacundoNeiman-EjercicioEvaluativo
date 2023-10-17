class Pelicula():

  def __init__(self, titulo, duracion, genero, id=None):
    self.titulo = titulo
    self.duracion = duracion
    self.genero = genero
    self.id = id

  def get_titulo(self):
    return self.titulo

  def get_id(self):
    return self.id

  def set_id(self, id):
    self.id = id

  def get_duracion(self):
    return self.duracion

  def get_genero(self):
    return self.genero

  def set_titulo(self, titulo):
    self.titulo = titulo

  def set_duracion(self, duracion):
    self.duracion = duracion

  def set_genero(self, genero):
    self.genero = genero

  def mostrar_info(self):
    return f"Película {self.get_id()} - Título: {self.get_titulo()}, Duración: {self.get_duracion()}, Género: {self.get_genero()}"
