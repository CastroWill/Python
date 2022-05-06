
def main():
    t1 = Triangulo(3, 3, 3)
    t2 = Triangulo(3, 4, 5)
    return print(t1.semelhantes(t2))

 
class Triangulo:
    def __init__(self, a, b, c):
        self.lados = [a, b, c]

    def perimetro(self):
        return self.lados[0] + self.lados[1] + self.lados[2]

    def tipo_lado(self):
        if self.lados[0] != self.lados[1] and self.lados[1] != self.lados[2] and self.lados[2] != self.lados[0]:
            return 'escaleno'
        if self.lados[0] == self.lados[1] and self.lados[1] == self.lados[2]:
            return 'equilátero'
        if self.lados[0] == self.lados[1] or self.lados[0] == self.lados[2] or self.lados[1] == self.lados[2]:
            return 'isósceles'

    def retangulo(self):
        hip, cat_adj, cat_opt = sorted(self.lados, reverse=True)
        if (cat_adj**2 + cat_opt**2) == (hip**2):
            return True
        else:
            return False
        
    def semelhantes(self, triangulo):
        for l in range(len(self.lados)):
            if self.lados[l] >= triangulo.lados[l]:
                if (self.lados[l] % triangulo.lados[l]) != 0:
                    return False
            elif self.lados[l] < triangulo.lados[l]:
                if (triangulo.lados[l] % self.lados[l]) != 0:
                    return False
            if l == 2:
                return True


if __name__ == '__main__':
    main()

