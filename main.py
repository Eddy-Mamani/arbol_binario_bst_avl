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
        print("5. Salir BST")
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
            break
        else:
            print("Opción inválida.")