def calcular_imc(peso, altura):
    resultado = peso/(altura**2)
    imc = round(resultado, 1)
    return imc
