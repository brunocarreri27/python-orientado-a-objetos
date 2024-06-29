class Pessoa:
    def __init__(self, sexo, peso):
        self.sexo = sexo
        self.peso = peso

    def calcularHomem(self):
          if self.sexo == "masculino":
                gasto_diario = (0.063 * self.peso + 2.896) * 239
                return gasto_diario
    
    def calcularMulher(self):
            if self.sexo == "feminino":
                gasto_diario = (0.062 * self.peso + 2.036) * 239
                return gasto_diario  