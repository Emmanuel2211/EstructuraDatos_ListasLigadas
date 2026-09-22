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
    por convención, un solo guion bajo al inicio del nombre indica que es un
    detalle de implementación interno, que no debería usarse desde fuera de
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
            - (Generator): Generador que devuelve los elementos contenidos en
            la lista
        """
        actual = self.__cabeza
        while actual is not None:
            yield actual.elemento
            actual = actual.siguiente

    # Métodos heredados de Coleccion

    def agregar(self, elemento: T) -> None:
        """
        Agrega un elemento al inicio de la lista

        return:
            - la misma ListaLigadaSimple con un elemento más
        """
        if elemento is None:
            raise TypeError("El nuevo elemento de la lista no puede ser nulo!")
        if self.__longitud == 0:
            self.__cabeza = _Nodo(elemento)
            self.__longitud += 1
            return None

        n_nodo = _Nodo(elemento)
        n_nodo.siguiente = self.__cabeza
        self.__cabeza = n_nodo
        self.__longitud += 1

    def eliminar(self, elemento: T) -> None:
        """
        Elimina la primera aparición del elementos a eliminar.

        return:
            - la misma lista pero con elemento deseado eliminado
        """
        if self.__cabeza is None:
            return None

        if elemento == self.__cabeza.elemento:
            self.__cabeza = self.__cabeza.siguiente
            self.__longitud -= 1
            return None

        actual = self.__cabeza
        while actual.siguiente is not None:
            if actual.siguiente.elemento == elemento:
                actual.siguiente = actual.siguiente.siguiente
                self.__longitud -= 1
                return None
            actual = actual.siguiente

    def buscar(self, elemento: T) -> bool:
        """
        Recorre la lista comparando cada elemento con el que se desea encontrar

        return:
            - Un booleano que represanta si el elemento se encutra en
            la lista (True) o no (False)
        """
        if self.__longitud == 0:
            return False

        for e in self:
            if e == elemento:
                return True
        return False

    # Métodos heredados de Lista

    def acceder(self, indice: int) -> T:
        """
        Recibe ListaLigadaSimple y un entero i, y verifica que el índice dado
        sea válido. Después recorre la lista y realiza un conte de los nodos
        hasta i.

        return:
            - el elemento en el nodo número i
        """
        if indice < 0 or indice >= self.__longitud:
            raise IndexError("Índice fuera de rango.")

        actual = self.__cabeza
        for _ in range(indice):
            actual = actual.siguiente
        return actual.elemento

    def eliminar_indice(self, indice: int) -> None:
        """
        Recibe ListaLigadaSimple y un entero i, y verifica que el índice dado
        sea válido. Después recorre la lista y cambia las referencias de los
        nodos adyacentes para eliminar ese nodo. Disminuye la longitud en uno.

        return:
            - el elemento en el nodo número con índice i eliminado
        """
        if indice < 0 or indice >= self.__longitud:
            raise IndexError("Índice fuera de rango.")

        if indice == 0:
            self.__cabeza = self.__cabeza.siguiente
            self.__longitud -= 1
            return None

        actual = self.__cabeza
        for _ in range(indice - 1):
            actual = actual.siguiente

        actual.siguiente = actual.siguiente.siguiente
        self.__longitud -= 1

    def devolver_indice_elemento(self, elemento: T) -> int:
        """
        Recibe ListaLigadaSimple y un elemento. si la lista es vacia devuelve
        error. Sino, recorre la lista hasta encontrar al elemento deseado
        mientras va contando los nodos recorridos.

        return:
            - Si encuentra el elemento, devuelve el conteo que tiene en ese
            momento.
        """
        if self.__longitud == 0:
            raise ValueError("La lista está vacía.")

        indice = 0
        for e in self:
            if e == elemento:
                return indice
            indice += 1

        raise ValueError(f"El elemento {elemento} no se encuentra en la lista.")

    def devolver_longitud(self) -> int:
        """
        Recie una ListaLigadaSimple y devuelve el atribut longitud.

        return:
            - int longitud de ListaLigadaSimple
        """
        return self.__longitud

    def __str__(self) -> str:
        """
        Devuelve la representación en texto de la lista con el formato:
        elem1 -> elem2 -> elem3

        Returns:
            str:
                Representacion en cadena de la lista
        """
        return " -> ".join(str(elemento) for elemento in self)
