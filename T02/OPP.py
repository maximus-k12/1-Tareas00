
"""**************************Matrices POO*******************************"""
class matrices(object):
    """Constructor de la clase
       todos los metodos dentro del objeto, 
       llevan el parametro inicial."""
    row_01 = 0
    colm_01 = 0
    cantidad_elementos = None

    def __init__(self, n, m): #Inicializamos la matrix para cada posicion en 0.
        self.row_01 = n
        self.colm_01 = m
        self.cantidad_elementos = []
        for i in range(self.row_01):
            self.cantidad_elementos.append([])
            for j in range(self.colm_01):
                self.cantidad_elementos[i].append(0)

    def elementos(self, i, j, v): #Reescribir cada valor con su respectiva celda.
        self.cantidad_elementos[i][j] = v

    def define_row(self, i, v): #Reescribir el valor para una fila completa.
        self.cantidad_elementos[i] = v

    def show_matrix(self): #Mostrar los valores almacenados para la matrix.
        for i in range(self.row_01):
            for j in range(self.colm_01): #Mostrar la matriz. 
                print("| {0} ".format(self.get_value_of_position(i, j)), sep=',', end='')
            print('|\n')

    def get_cols(self): #Retorna el No de columnas para matriz.
        return self.colm_01

    def get_rows(self): #Retorna el No de filas para matriz.
        return self.row_01

    def get_value_of_position(self, i, j): #Rerornar el valor para fila y columna.
        return self.cantidad_elementos[i][j] #Cada valor en fila (i) y colummna (j).

    def add(self, *matrix): #Funcion que recibe varias matrices como argumentos.
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                tmp = self.get_value_of_position(i, j)
                for m in matrix:
                    tmp += m.get_value_of_position(i, j)
                row.append(tmp)
            yield row

    def scalar_product(self, x): #Para x: No Real.
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.get_value_of_position(i, j)*x)
            yield row

    def product(self, m): #Recibir una matriz como argumento otra vez.
        if self.rows is not m.cols:
            raise Exception('Numero de filas'
                            'y el numero de columnas'
                            "no coinciden")
        for i in range(self.rows):
            row = []
            for j in range(m.cols):
                add = 0
                for c in range(self.cols):
                    add += self.get_value_of_position(i, c) * \
                           m.get_value_of_position(c, j)
                row.append(add)
            yield row

    def transpose(self):
        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.get_value_of_position(i, j))
            yield row

    cols = property(fget=get_cols)
    rows = property(fget=get_rows)

matrix1 = matrices(2,3)
"""******************Primera fila*********************"""
matrix1.elementos(0,0,1)
matrix1.elementos(0,1,2)
matrix1.elementos(0,2,3)
"""*******************Segunda fila********************"""
matrix1.elementos(1,0,7)
matrix1.elementos(1,1,8)
matrix1.elementos(1,2,9)
 
matrix2 = matrices(3,2)
"""*****************Primera columna*******************"""
matrix2.elementos(0,0,1)
matrix2.elementos(1,0,7)
matrix2.elementos(2,0,13)
"""*****************Segunda columna*******************"""
matrix2.elementos(0,1,2)
matrix2.elementos(1,1,8)
matrix2.elementos(2,1,14)
 
matrix3 = matrices(matrix1.get_rows(), matrix2.get_cols())
i = 0
for e in matrix1.product(matrix2):
    matrix3.define_row(i, e)
    i = i + 1

print(matrix3.show_matrix())