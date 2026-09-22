"""
Módulo lista_ligada_simple
"""

from typing import Iterator, Optional, TypeVar, Generic
from lista import Lista

T = TypeVar("T")


class _Nodo(Generic[T]):
    """
    Nodo interno de la lista ligada simple.

    En Python no existe un modificador de acceso "privado" 
    por convención, un solo guion bajo al inicio del nombre indica que es un detalle
    de implementación interno, que no debería usarse desde fuera de
    la clase.

    Args: 
        elemento (T): Elemento contenido en el nodo.
        siguiente (_Nodo[T]): Nodo siguiente. Opcional.
    """

    # Permite asegurar acceso rapido y memoría eficiente. 
    # Evita la creación de atributos extras
    __slots__ = ("elemento", "siguiente")

    def __init__(self, elemento: T):
        self.elemento: T = elemento
        self.siguiente: Optional[_Nodo[T]] = None


class ListaLigadaSimple(Lista[T]):

    def __init__(self) -> None:
        self.__cabeza: Optional[_Nodo[T]] = None
        self.__longitud: int = 0


    def __iter__(self) -> Iterator[T]:
        """
        Permite recorrer la lista con 'for elemento in lista:'.

        returns: 
            - (Generator): Generador que devuelve los elementos contenidos en la lista
        """
        actual = self.__cabeza
        while actual is not None:
            yield actual.elemento
            actual = actual.siguiente



    # Métodos heredados de Coleccion

    def agregar(self, elemento: T) -> None:
        # TODO: Aquí va tu codigo        

    def eliminar(self, elemento: T) -> None:
        # TODO: Aquí va tu codigo

    def buscar(self, elemento: T) -> bool:
        # TODO: Aquí va tu codigo

    # Métodos heredados de Lista

    def acceder(self, indice: int) -> T:
        # TODO: Aquí va tu codigo

    def eliminar_indice(self, indice: int) -> None:
        # TODO: Aquí va tu codigo

    def devolver_indice_elemento(self, elemento: T) -> int:
        # TODO: Aquí va tu codigo

    def devolver_longitud(self) -> int:
        # TODO: Aquí va tu codigo
    

    def __str__(self) -> str:
        """
        Devuelve la representación en texto de la lista con el formato:
        elem1 -> elem2 -> elem3

        Returns: 
            str: 
                Representacion en cadena de la lista
        """
        # TODO: Aquí va tu codigo

    

