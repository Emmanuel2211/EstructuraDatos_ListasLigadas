"""
Módulo de pruebas
==================

Módulo para probar la implementación de `ListaLigadaSimple`.
"""
from lista_ligada_simple import ListaLigadaSimple as LS
import random

class MainListaSimple():

    def main(self) -> None:

        lista : LS[int] = LS[int]()
        print(f"Lista: {lista}")
        print(f"Longitud: {len(lista)}")

        for _ in range(25):
            i : int = random.randint(0,500)
            print("Agregando elemento ...")
            lista.agregar(i)
            print(f"Lista: {lista}")
            print(f"Longitud: {len(lista)}")

        num1: int = random.randint(0,500)
        print(f"¿{num1} está en {lista}?: {num1 in lista}")

        print(f"Elemento en 7: {lista[7]}")

        print(f"Elimina elemento en 10 ...")

        lista.eliminar_indice(10)

        print(f"Lista: {lista}")
        print(f"Longitud: {len(lista)}")

        num2: int = random.randint(0,10)

        print(f"Eliminar {num2} de {lista} ...")
        lista.eliminar(num2)

        print(f"Lista: {lista}")
        print(f"Longitud: {len(lista)}")

if __name__ == "__main__":
    m = MainListaSimple()
    m.main()


        
