import menu
from menu.opciones import generar_menu


def menu_principal():
    opciones = {
        "1": ("Añadir", agregar),
        "2": ("Buscar", buscar),
        "3": ("Modificar", modificar),
        "4": ("Eliminar", eliminar),
        "5": ("Mostrar", mostrar),
        "9": ("Salir", salir)
    }

    generar_menu(opciones, '9')


def mostrar():
    print('Mostrando...')
    print()


def agregar():
    print('Añadiendo...')
    print()


def buscar():
    print('Buscando...')
    print()


def modificar():
    print('Modificando...')
    print()


def eliminar():
    print('Eliminando...')
    print()


def salir():
    print('Saliendo...')
    print()


if __name__ == '__main__':
    print('Título')
    menu_principal()
