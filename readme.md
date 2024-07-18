# Do que se trata esse projeto
- Este programa python simplesmente calcula o imc(índice de massa corporal) de uma pessoa.

- Conta com uma GUI (interface gráfica).

# Porque eu usaria este programa
- Um programa muito útil caso você deseje identificar sua situação em relação ao seu peso, de forma rápida e eficiente.

- Conta com uma interface gráfica, o que auxilia na produtividade, dinâmica e acessibilidade do programa.

- Pode ser facilmente adaptado para automações, podendo fazer diversas consultas em questão de segundos.

# Como funciona
- Rode o programa com a linha:
```python app.py```

- Em seguida preencha os campos:
    -  Peso
    -  Altura

- Isto resulta em um cálculo interno e ao finaliza-lo, são retornados na tela:
    - O resultado numérico (IMC em sí).
    - A categoria que este número indica.

- As categorías possuem cores relativas ao gral de risco que aquela situação representa
Por exemplo:

    - O gral perigoso para pesos baixos é representado pela cor branca
    - O gral ideal é representado pela cor verde
    - O gral mais perigoso para pesos altos é representado pela cor laranja escuro
    - Entre outras cores e categorias

# Detalhes técnicos
- Estas categorias utilizadas são definidas internamente no módulo: ```categorias.py```,
atravez de instâncias da classe ```Categoria```, que por tanto, podem ser "customizadas" com:

  - Diferentes códigos de cores.
  - Apelidos.
  - Parâmetros de intervalo (altura/peso máximo e mínimo), responsávies por definir os IMCs que enquadram aquela categoria. Obs: Os
    valores padrão seguem as tableas atuais indicadas pelos orgãos de saúde.

# Dependências
- Você pode verificar as bibliotecas necessárias para o funcionamento no módulo ```requirements.txt```
- Ou simplesmente instale todas as bibliotecas necessárias atravez do comando: ```pip install -r requirements.txt```
