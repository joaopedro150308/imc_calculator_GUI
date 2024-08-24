from dataclasses import dataclass

@dataclass
class Categoria():
    nome: str
    valor_minimo: float or None # type: ignore
    valor_maximo: float or None # type: ignore
    estado: str
    text_color: str


    def verificar_se_pertence_a_categoria(self, imc):

        # Caso os valores máximo ou minimos sejam indefinidos
        if self.valor_minimo is None:
            if imc <= self.valor_maximo:
                return True
        elif self.valor_maximo is None:
            if imc >= self.valor_minimo:
                return True
        
        # Caso sejam definidos
        else:
            if imc >= self.valor_minimo and imc <= self.valor_maximo:
                return True
            else:
                return False
