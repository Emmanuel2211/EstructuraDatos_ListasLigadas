from typing import TypeVar, Generic

T = TypeVar("T")


class _PruebaYeah(Generic[T]):
    def __init__(self, valor_uno: T, valor_dos: T):
        self.__dato: T = valor_uno
        self.dato2: T = valor_dos

    def actualizar(self, nuevo_valor: T, nuevo_valor2: T) -> None:
        self.__dato = nuevo_valor
        self.dato2 = nuevo_valor2

    def devolver(self) -> None:
        print(self.__dato, self.dato2)

    def mostrar_tipo_real(self) -> None:
        print(
            f"El tipo actual del dato1 es: {type(self.__dato)} el tipo del dato2 es: {type(self.dato2)}"
        )


x = _PruebaYeah(20, 30)
x.mostrar_tipo_real()

print(x.dato2)
# print(x.__dato) # this will be an error __ (private "kinda")



y = _PruebaYeah("este si", True)
y.mostrar_tipo_real()
y.mostrar_tipo_real()
