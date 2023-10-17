from modulos.Pelicula import Pelicula


class PeliculaAnimada(Pelicula):

  def __init__(self, titulo, duracion, genero, estudioAnimacion, id=None):
    super().__init__(titulo, duracion, genero, id)
    self.estudioAnimacion = estudioAnimacion

  def get_estudioAnimacion(self):
    return self.estudioAnimacion

  def set_estudioAnimacion(self, estudioAnimacion):
    self.estudioAnimacion = estudioAnimacion

  def mostrar_info(self):
    return f"Película {self.get_id()} - Título: {self.get_titulo()}, Duración: {self.get_duracion()}, Género: {self.get_genero()}, Estudio de animacion: {self.get_estudioAnimacion()}"
