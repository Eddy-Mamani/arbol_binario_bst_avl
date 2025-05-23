class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierdo), self.obtener_altura(nodo.derecho))

    def obtener_balance(self, nodo):
        return self.obtener_altura(nodo.izquierdo) - self.obtener_altura(nodo.derecho) if nodo else 0

    def rotar_derecha(self, y):
        x = y.izquierdo
        T2 = x.derecho
        x.derecho = y
        y.izquierdo = T2
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        return x

    def rotar_izquierda(self, x):
        y = x.derecho
        T2 = y.izquierdo
        y.izquierdo = x
        x.derecho = T2
        self.actualizar_altura(x)
        self.actualizar_altura(y)
        return y