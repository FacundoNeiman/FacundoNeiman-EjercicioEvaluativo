import sqlite3
from modulos.PeliculaAnimada import PeliculaAnimada
from modulos.Cine import Cine
from modulos.Pelicula import Pelicula


class Conexion:

  def __init__(self, nombre_base_datos):
    self.conexion = sqlite3.connect(nombre_base_datos)
    self.cursor = self.conexion.cursor()

  def crearTablas(self):
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS peliculas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    duracion INTEGER,
    genero TEXT,
    estudio_animacion TEXT,
    animada INTEGER
    )''')

    self.cursor.execute('''CREATE TABLE IF NOT EXISTS cines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    direccion TEXT
    )''')

    self.conexion.commit()

  def agregarPelicula(self, pelicula):
    if isinstance(pelicula, PeliculaAnimada):
      estudio_animacion = pelicula.get_estudioAnimacion()
      animada = 1
    else:
      estudio_animacion = None
      animada = 0

    self.cursor.execute(
        '''INSERT INTO     
    peliculas(titulo,duracion,genero,estudio_animacion,animada)       VALUES       (?,?,?,?,?)''',
        (pelicula.get_titulo(), pelicula.get_duracion(), pelicula.get_genero(),
         estudio_animacion, animada))
    self.conexion.commit()

  def agregarCine(self, cine):
    self.cursor.execute(
        '''INSERT INTO     
    cines(nombre,direccion)       VALUES       (?,?)''',
        (cine.get_nombre(), cine.get_direccion()))
    self.conexion.commit()

  def listarPeliculas(self):
    self.cursor.execute('''SELECT * from peliculas''')
    peliculas = self.cursor.fetchall()
    for pelicula in peliculas:
      if pelicula[4] is not None:
        aux = PeliculaAnimada(pelicula[1], pelicula[2], pelicula[3],
                              pelicula[4], pelicula[0])
      else:
        aux = Pelicula(pelicula[1], pelicula[2], pelicula[3], pelicula[0])
      print(aux.mostrar_info())

  def listarCines(self):
    self.cursor.execute('''SELECT * from cines''')
    cines = self.cursor.fetchall()
    for cine in cines:
      aux = Cine(cine[1], cine[2], cine[0])
      print(aux.mostrar_info())

  def cerrarConexion(self):
    self.cursor.close()
    self.conexion.close()

  def modificarPelicula(self, pelicula):
    print(pelicula.mostrar_info())
    if isinstance(pelicula, PeliculaAnimada):
      estudio_animacion = pelicula.get_estudioAnimacion()
      animada = 1
    else:
      estudio_animacion = None
      animada = 0
    self.cursor.execute(
        '''UPDATE peliculas SET titulo=?, duracion=?, genero=?, 
    estudio_animacion = ?, animada = ? WHERE 
    id=?''',
        (pelicula.get_titulo(), pelicula.get_duracion(), pelicula.get_genero(),
         estudio_animacion, animada, pelicula.get_id()))
    self.conexion.commit()

  def modificarCine(self, cine):
    self.cursor.execute(
        '''UPDATE cines SET nombre=?, direccion=? WHERE 
    id=?''', (cine.get_nombre(), cine.get_direccion(), cine.get_id()))
    self.conexion.commit()

  def eliminarPelicula(self, id):
    self.cursor.execute('''DELETE FROM peliculas WHERE id = 
     ?''', (id, ))
    self.conexion.commit()

  def eliminarCine(self, id):
    self.cursor.execute('''DELETE FROM cines WHERE id = 
      ?''', (id, ))
    self.conexion.commit()

  def getPelicula(self, id):
    self.cursor.execute('''SELECT * from peliculas WHERE id = ?''', (id, ))
    pelicula = self.cursor.fetchmany(1)
    if pelicula:
      pelicula = pelicula[0]
      if pelicula[4] is None:
        aux = Pelicula(pelicula[1], pelicula[2], pelicula[3], pelicula[0])
      else:
        aux = PeliculaAnimada(pelicula[1], pelicula[2], pelicula[3],
                              pelicula[4], pelicula[0])
      return aux
    else:
      return None

  def getCine(self, id):
    self.cursor.execute('''SELECT * from cines WHERE id = ?''', (id, ))
    cine = self.cursor.fetchmany(1)
    if cine:
      cine = cine[0]
      aux = Cine(cine[1], cine[2], cine[0])
      return aux
    else:
      return None
