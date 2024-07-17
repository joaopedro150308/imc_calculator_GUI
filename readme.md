# Do que se trata esse projeto
    - Este programa python simplesmente calcula o imc(índice de massa corporal) de uma pessoa.
    - Conta com uma GUI (interface gráfica).
# Porque eu usaria este programa
    - Um programa muito útil caso você deseje identificar rapidamente sua situação em relação ao seu peso, de forma rápida e eficiente.
    - Conta com uma interface gráfica, o que auxilia na produtividade, dinâmica e acessibilidade do programa.
    - Pode ser facilmente adaptado para automações, podendo fazer diversas consultas em questão de segundos.
# Funcionalidades
    - O programa funciona de forma bem simples. Basta preencher os campos inputs: peso e altura (que aceitam apenas números), em seguida 
    clicar em ok.
    - Isto resulta em um cálculo interno e ao finaliza-lo, são retornados na tela o resultado numérico (IMC em sí) e a categoria que este
    número indica (de acordo com as tabelas que abordam este assunto).
    - As categorías possuem cores relativas ao gral de risco que aquela situação representa. Por exemplo: O gral perigoso para pesos baixos
    é representado pela cor branca, o gral ideal representado pela cor verde e o gral mais perigoso para pesos altos sendo representado pelo laranja escuro.
# Detalhes técnicos
    - Estas categorias utilizadas são definidas internamente no módulo "categorias.py", atravez de instâncias da classe "Categoria", que 
    por tanto, podem ser "customizadas" com:
        - Diferentes códigos de cores.
        - Apelidos.
        - Parâmetros de intervalo (altura/peso máximo e mínimo), responsávies por definir os IMCs que enquadram aquela categoria. Obs: Os
        valores padrão seguem as tableas atuais indicadas pelos orgãos de saúde.
