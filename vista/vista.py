import sqlite3 as sql
from base_datos.conexion import Conexion
from modulos.Pelicula import Pelicula
from modulos.PeliculaAnimada import PeliculaAnimada
from modulos.Cine import Cine

conexion = Conexion("base_datos/mi_bd.db")


def menu():
  while True:
    print("Seleccione una opción:")
    print("")
    print("Cine: ")
    print("1. Agregar un cine")
    print("2. Modificar cine")
    print("3. Eliminar cine")
    print("4. Listar cines")
    print("")
    print("Pelicula: ")
    print("5. Agregar película")
    print("6. Modificar película")
    print("7. Eliminar película")
    print("8. Listar películas")
    print("")
    print("Programacion: ")
    print("9. Ver programación del cine")
    print("10. Agregar película a programación")
    print("")
    print("0. Salir")
    opcion = int(input())

    if opcion == 0:
      print("Hasta luego! :)")
      break

    elif opcion == 1:
      agregarCine()

    elif opcion == 2:
      modificarCine()

    elif opcion == 3:
      eliminarCine()

    elif opcion == 4:
      listarCines()

    elif opcion == 5:
      agregarPelicula()

    elif opcion == 6:
      modificarPelicula()

    elif opcion == 7:
      eliminarPelicula()

    elif opcion == 8:
      listarPeliculas()

    elif opcion == 9:
      listarProgramacion()

    elif opcion == 10:
      agregarPeliculaProgramacion()

    else:
      print("Comando inválido. Intente nuevamente ")

    print("")
    print("")


def agregarCine():
  cine = Cine(input("Ingrese el nombre del cine "),
              input("Ingrese la dirección "))
  conexion.agregarCine(cine)
  print("Cine agregado correctamente ")


def modificarCine():
  id = int(input("Ingrese el id del cine a modificar "))
  aux = conexion.getCine(id)
  print(f"Datos del cine - {id}:")
  print(aux.mostrar_info())
  cine = Cine(input("Ingrese el nombre del cine "),
              input("Ingrese la dirección"), id)
  conexion.modificarCine(cine)
  print("Cine modificado correctamente ")


def eliminarCine():
  id = int(input("Ingrese el id del cine a eliminar "))
  conexion.eliminarCine(id)
  print("Cine eliminado correctamente ")


def listarCines():
  print("Cines: ")
  conexion.listarCines()


def agregarPelicula():
  titulo = input("Ingrese el título de la pelicula ")
  duracion = int(input("Ingrese la duración en minutos "))
  genero = input("Ingrese el género ")
  estudio = input(
      "Si es una pelicula animada ingrese el estudio de animación, caso contrario ingrese 'X' "
  )
  if estudio.upper() == "X":
    pelicula = Pelicula(titulo, duracion, genero)

  else:
    pelicula = PeliculaAnimada(titulo, duracion, genero, estudio)

  conexion.agregarPelicula(pelicula)
  print("Película agregada correctamente ")


def modificarPelicula():
  id = int(input("Ingrese el id de la película a modificar "))
  aux = conexion.getPelicula(id)
  print(f"Datos de la pelicula - {id}:")
  print(aux.mostrar_info())
  if isinstance(aux, PeliculaAnimada):
    pelicula = PeliculaAnimada(input("Ingrese el título de la pelicula "),
                               int(input("Ingrese la duración en minutos ")),
                               input("Ingrese el género "),
                               input("Ingrese el estudio "), id)
  else:
    pelicula = Pelicula(input("Ingrese el título de la pelicula "),
                        int(input("Ingrese la duración en minutos ")),
                        input("Ingrese el género "), id)
  conexion.modificarPelicula(pelicula)
  print("Película modificada correctamente ")


def eliminarPelicula():
  id = int(input("Ingrese el id de la película a eliminar "))
  conexion.eliminarPelicula(id)
  print("Película eliminada correctamente ")


def listarPeliculas():
  print("Peliculas: ")
  conexion.listarPeliculas()


def listarProgramacion():
  listarCines()
  id = int(
      input("Ingrese el id del cine del cual quiere ver la programación: "))
  cine = conexion.getCine(id)
  print("")
  cine.mostrar_programacion()
  print("")


def agregarPeliculaProgramacion():
  listarCines()
  id = int(
      input(
          "Ingrese el id del cine al cual quiere agregar una pelicula a su programación: "
      ))
  cine = conexion.getCine(id)
  print("")
  listarPeliculas()
  id = int(input("Ingrese el id de la película a agregar "))
  pelicula = conexion.getPelicula(id)
  conexion.agregarProgramacion(cine.get_id(), pelicula.get_id())
  print(
      f"Película añadida a la programación del {cine.get_nombre()} correctamente "
  )
