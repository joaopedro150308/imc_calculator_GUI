from dataclasses import dataclass

@dataclass
class Categoria():
    nome: str
    valor_minimo: float or None
    valor_maximo: float or None
    estado: str
    text_color: str


    def verificar_se_pertence_a_categoria(self, imc):

        # Caso os valores máximo ou minimos sejam indefinidos
        if self.valor_minimo == None:
            if imc < self.valor_maximo:
                return True
        elif self.valor_maximo == None:
            if imc > self.valor_minimo:
                return True
        
        # Caso sejam definidos
        else:
            if imc >= self.valor_minimo and imc <= self.valor_maximo:
                return True
            else:
                return False
