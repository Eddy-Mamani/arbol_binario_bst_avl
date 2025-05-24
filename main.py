from arbol_bst import ArbolBST
from arbol_avl import ArbolAVL

def menu_bst():
    arbol = ArbolBST()
    while True:
        print("\n--- Árbol BST ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Mostrar Inorden")
        print("5. Mostrar altura")
        print("6. Salir BST")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            valor = int(input("Valor a insertar: "))
            arbol.insertar(valor)
            print("Insertado.")
        elif opcion == "2":
            valor = int(input("Valor a buscar: "))
            encontrado = arbol.buscar(valor)
            print("Encontrado." if encontrado else "No encontrado.")
        elif opcion == "3":
            valor = int(input("Valor a eliminar: "))
            arbol.eliminar(valor)
            print("Eliminado (si existía).")
        elif opcion == "4":
            print("Inorden:", arbol.inorden())
        elif opcion == "5":
            print("altura del arbol bst:", arbol.altura())
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

def menu_avl():
    arbol = ArbolAVL()
    while True:
        print("\n--- Árbol AVL ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Mostrar Inorden")
        print("5. mostrar altura")
        print("6. Salir AVL")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            valor = int(input("Valor a insertar: "))
            arbol.insertar(valor)
            print("Insertado.")
        elif opcion == "2":
            valor = int(input("Valor a buscar: "))
            encontrado = arbol.buscar(valor)
            print("Encontrado." if encontrado else "No encontrado.")
        elif opcion == "3":
            valor = int(input("Valor a eliminar: "))
            arbol.eliminar(valor)
            print("Eliminado (si existía).")
        elif opcion == "4":
            print("Inorden:", arbol.inorden())
        elif opcion == "5":
            print("altura del arbol avl:", arbol.altura())
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

def main():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Trabajar con Árbol BST")
        print("2. Trabajar con Árbol AVL")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_bst()
        elif opcion == "2":
            menu_avl()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
