############################################################
# Dados da Equipe
############################################################
# Danilo Santos Ribeiro
# Davi Klayver Dantas Lima
# Turma 07
# Graficos sorteados: 
# Gráfico de linhas: L3 
# Gráfico de barras: B12
# Gráfico de boxplot: X12	
# Resposta Textual: T7
# Proposta: Gráfico de Barras: Quais foram os <X> países com os maiores números de medalhas no <ano>? 
############################################################
# Arquivos com bibliotecas definidas pelo(a) programador(a)
############################################################


from termcolor import colored
from Graficos.Textual import textual
from Graficos.Linhas import linhas
from Graficos.Boxplot import boxplot
from Graficos.Barras import barras
from Graficos.Proposta import proposta
from Graficos.Suporte import limparTela, encontrar_anos_participados, esportes_existentes

def iniciar():
    print(colored('«»'*17+'|'+'«»'*17,attrs=['dark']))
    print(
        colored(
            'ESCOLHA UMA OPÇÃO DE GRÁFICO, RESPOSTA TEXTUAL OU PROPOSTA PARA SER EXIBIDO:',
            'magenta'))
    print(colored('«»'*17+'|'+'«»'*17,attrs=['dark']))
    print(colored('[0]', 'yellow'), 'GRÁFICO DE LINHAS')
    print(colored('[1]', 'yellow'), 'GRÁFICO DE BARRAS')
    print(colored('[2]', 'yellow'), 'GRÁFICO BOXPLOT')
    print(colored('[3]', 'yellow'), 'TEXTUAL')
    print(colored('[4]', 'yellow'), 'PROPOSTA')
    print(colored('[5]', 'yellow'), 'SAIR')
    print(colored('«»'*17+'|'+'«»'*17,attrs=['dark']))
    return input().strip()



#ESCOLHA DO TIPO DE RESPOSTA E CHAMANDO SUA RESPECTIVA FUNÇÃO
while True:
  tipo_de_grafico_escolhido=iniciar()
  limparTela()
  if tipo_de_grafico_escolhido=='0':
    linhas({})
  elif tipo_de_grafico_escolhido=='1':
    barras({'lista_esportes_existentes':esportes_existentes()})
  elif tipo_de_grafico_escolhido=='2':
    boxplot({'lista_esportes_existentes':esportes_existentes()})
  elif tipo_de_grafico_escolhido=='3':
    textual()
  elif tipo_de_grafico_escolhido=='4':
    proposta({'anos_disponiveis':encontrar_anos_participados('','','')})
  elif tipo_de_grafico_escolhido=='5':
    break
  else:
    print(colored('POR FAVOR DIGITE UM NÚMERO VÁLIDO', 'red',attrs=['bold','reverse']))

print(colored('«»'*17+'|'+'«»'*17,attrs=['dark'])) 
print(colored(" "*26+"Programa Finalizado",'red'))
print(colored('«»'*17+'|'+'«»'*17,attrs=['dark']))
print(colored("Este programa foi desenvolvido por:",'yellow'))
print(colored("Danilo Santos Ribeiro",'green'))
print(colored("Davi Klayver Dantas Lima",'green'))
print(colored('«»'*17+'|'+'«»'*17,attrs=['dark']))
print(colored(" "*30+"OBRIGADO!",'red')+colored(':D','blue'))
print(colored('«»'*17+'|'+'«»'*17,attrs=['dark'])) 