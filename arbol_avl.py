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

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoAVL(valor)
            return
        pila = []
        actual = self.raiz
        while True:
            pila.append(actual)
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = NodoAVL(valor)
                    pila.append(actual.izquierdo)
                    break
                actual = actual.izquierdo
            elif valor > actual.valor:
                if actual.derecho is None:
                    actual.derecho = NodoAVL(valor)
                    pila.append(actual.derecho)
                    break
                actual = actual.derecho
            else:
                return  

        for i in range(len(pila) - 1, -1, -1):
            nodo = pila[i]
            self.actualizar_altura(nodo)
            balance = self.obtener_balance(nodo)

            if balance > 1:
                if valor < nodo.izquierdo.valor:
                    nuevo = self.rotar_derecha(nodo)
                else:
                    nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
                    nuevo = self.rotar_derecha(nodo)
            elif balance < -1:
                if valor > nodo.derecho.valor:
                    nuevo = self.rotar_izquierda(nodo)
                else:
                    nodo.derecho = self.rotar_derecha(nodo.derecho)
                    nuevo = self.rotar_izquierda(nodo)
            else:
                continue

            if i == 0:
                self.raiz = nuevo
            else:
                padre = pila[i - 1]
                if padre.izquierdo == nodo:
                    padre.izquierdo = nuevo
                else:
                    padre.derecho = nuevo

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

    def obtener_minimo(self, nodo):
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual

    def eliminar(self, valor):
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
                temp = self.obtener_minimo(nodo.derecho)
                nodo.valor = temp.valor
                nodo.derecho = _eliminar(nodo.derecho, temp.valor)

            self.actualizar_altura(nodo)
            balance = self.obtener_balance(nodo)

            if balance > 1:
                if self.obtener_balance(nodo.izquierdo) >= 0:
                    return self.rotar_derecha(nodo)
                else:
                    nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
                    return self.rotar_derecha(nodo)
            if balance < -1:
                if self.obtener_balance(nodo.derecho) <= 0:
                    return self.rotar_izquierda(nodo)
                else:
                    nodo.derecho = self.rotar_derecha(nodo.derecho)
                    return self.rotar_izquierda(nodo)
            return nodo

        self.raiz = _eliminar(self.raiz, valor)

    def inorden(self):
        resultado = []
        pila = []
        actual = self.raiz
        while pila or actual:
            while actual:
                pila.append(actual)
                actual = actual.izquierdo
            actual = pila.pop()
            resultado.append(actual.valor)
            actual = actual.derecho
        return resultado