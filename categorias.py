from calsses import Categoria

muito_abaixo = Categoria('M_A', None, 16.9, 'Muito abaixo', '#F8F8FF')

abaixo = Categoria('A', 17, 18.5, 'Abaixo do peso', '#90EE90')

normal = Categoria('N', 18.5, 24.9, 'Peso normal', '#008000')

acima = Categoria('A', 25, 29.9, 'Acima do peso', '#F0E68C')

obesidade1 = Categoria('O1', 30, 34.9, 'Obesidade', '#FFA500')

obesidade2 = Categoria('O2', 35, 39.9, 'Obesidade II', '#FF8C00')

obesidade3 = Categoria('O3', 40, None, 'Obesidade III', '#FF4500')

categorias_lista = [muito_abaixo, abaixo, normal, acima, obesidade1, obesidade2, obesidade3]

def encontrar_categoria(imc):
    for categoria in categorias_lista:
        verificar = categoria.verificar_se_pertence_a_categoria(imc=imc)
        if verificar == True:
            return categoria
