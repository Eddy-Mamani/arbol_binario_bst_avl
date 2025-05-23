class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoBST(valor)
            return
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = NodoBST(valor)
                    return
                actual = actual.izquierdo
            elif valor > actual.valor:
                if actual.derecho is None:
                    actual.derecho = NodoBST(valor)
                    return
                actual = actual.derecho
            else:
                return 
            
    def buscar(self, valor):
        actual = self.raiz
        while actual:
            if valor == actual.valor:
                return True
            elif valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return False

    def eliminar(self, valor):
        def _minimo(nodo):
            while nodo.izquierdo:
                nodo = nodo.izquierdo
            return nodo

        def _eliminar(nodo, valor):
            if nodo is None:
                return None
            if valor < nodo.valor:
                nodo.izquierdo = _eliminar(nodo.izquierdo, valor)
            elif valor > nodo.valor:
                nodo.derecho = _eliminar(nodo.derecho, valor)
            else:
                if nodo.izquierdo is None:
                    return nodo.derecho
                elif nodo.derecho is None:
                    return nodo.izquierdo
                temp = _minimo(nodo.derecho)
                nodo.valor = temp.valor
                nodo.derecho = _eliminar(nodo.derecho, temp.valor)
            return nodo

        self.raiz = _eliminar(self.raiz, valor)