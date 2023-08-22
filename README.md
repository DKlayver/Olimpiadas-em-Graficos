# Python

https://replit.com/@PI-01/Projeto01xitado

O projeto visa a partir de três arquivos CSV, gerar gráficos com informações úteis sobre as Olímpiadas. O usuário irá através de um menu selecionar qual gráfico deseja e como.

O arquivo athlete_events.csv contém 271.116 linhas e 15 colunas. Cada linha corresponde a um atleta individual competindo em um evento olímpico individual. As colunas são:

  ID - Identificador único para cada Atleta
  Name - Nome do atleta
  Sex - Sexo (M ou F)
  Age - Idade (Inteiro)
  Height - Altura (Em centímetros)
  Weight - Peso (Em quilogramas) *o correto seria massa
  Team - Nome da Equipe
  NOC - National Olympic Committee (código de 3 letras)
  Games - Ano e Temporada (Inverno ou Verão)
  Year - Ano (Inteiro)
  Season (Temporada) - Summer ou Winter
  City - Cidade Sede
  Sport - Esporte
  Event - Evento
  Medal - Ouro, Prata, Bronze ou NA

Já o arquivo noc_regions.csv contém 230 linhas e 3 colunas. Cada linha representa um membro do comitê olímpico internacional, com o seu código, nome do país e um comentário sobre o nome do país.

No arquivo countries-continents.csv contém 195 linhas e 2 colunas. Cada linha representa o
nome de um país e seu respectivo continente.

=================================================================================================================================================================================================

Gráfico de Linhas:
  Desempenho do <País> nas últimas <X> olimpíadas de <Tipo de Olimpíada>, três
linhas, uma por cada tipo de medalha.

Gráfico de Barras:
  Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano>
de <Tipo de Olimpíada>, separados por sexo.

Gráfico Boxplot:
  Peso dos atletas do <Esporte> nas últimas <X> olimpíadas de <Tipo de
Olimpíada>.

Resposta Textual:
  Vencedores de medalhas em diferentes esportes numa mesma olimpíada.

Proposta:
  Barras: Quais foram os <X> países com os maiores números de atletas medalhista no <ano> ? 
  
=================================================================================================================================================================================================

Se necessário, use os comandos no terminal para instalar as dependencias:

  python3 -m pip install --upgrade termcolor
  
  pip install matplotlib
