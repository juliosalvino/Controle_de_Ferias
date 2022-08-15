"""
verificações necessárias:

verificar se o nome já está gravado, se estiver, mostrar as opções na tela e perguntar se quer colocar uma
 nova data,
se sim, seguir com as demais opções, se não, ir direto para a opção de encerrar ou reiniciar a gravação
identificar se a diferença de entrada e saida é maior que 30 dias (se for maior, mensagem de erro)
identificar se a entrada é em um dos dias que não pode (se for, mensagem de erro)
identificar se tem alguma pessoa daquele mesmo setor tirando férias naquele período (só pode 1 por setor)

caso preencha todos os requisitos, dar a opção de gravar as férias (gravar no arquivo csv)

arquivo gravado, vai mostrar na tela o arquivo com a gravação e as demais do setor

opção de encerrar ou fazer uma nova gravação - feito
"""


import os
import datetime as dt
from tkinter.tix import COLUMN
import pandas as pd
import sys

def menu():
    print("****************Controle de Férias****************")
    print("\n")
    print("Bem vindo ao seu controle de férias, por aqui você consegue: \n")
    print("1 - Visualizar os pedidos de férias do seu setor.\n2 - Visualizar todos os feriados nacionais deste ano.\n3 - Entrar com um novo pedido de férias junto ao seu RH.\n4 - Sair.")


menu()

entrada = input("Digite a opção desejada: ")

#Entrada de pedido de férias, será gravado na planilha ferias.xlsx, na sheet pedidos_ao_rh

def pedidos_do_setor(): #quase pronto
    print("\n")
    print("Escolha o seu setor, e visualize os pedidos de férias já existentes.")
    print("\n")
    print("Setores disponíveis:\n1 - Marketing\n2 - Tecnologia\n3 - Logística\n4 - Produtos\n5 - Operações\n6 - Diretoria\n7 - Facilities")
    print("\n")
    input_setor = input("Digite o número do seu setor: ")
   
    #Separando por setores
    if input_setor == "1":
        df_xlsx = pd.read_excel(r"ferias.xlsx", sheet_name= "pedidos_ao_rh", engine= "openpyxl")
        df_filtrado = df_xlsx["Setor"] == "Marketing"
        print("\n")
        print(df_xlsx[df_filtrado])
        print("\n")     
    elif input_setor == "2":
        df_xlsx = pd.read_excel(r"ferias.xlsx", sheet_name= "pedidos_ao_rh", engine= "openpyxl")
        df_filtrado = df_xlsx["Setor"] == "Tecnologia"
        print("\n")
        print(df_xlsx[df_filtrado])
        print("\n")
    elif input_setor == "3":
        df_xlsx = pd.read_excel(r"ferias.xlsx", sheet_name= "pedidos_ao_rh", engine= "openpyxl")
        df_filtrado = df_xlsx["Setor"] == "Logística"
        print("\n")
        print(df_xlsx[df_filtrado])
        print("\n")
    elif input_setor == "4":
        df_xlsx = pd.read_excel(r"ferias.xlsx", sheet_name= "pedidos_ao_rh", engine= "openpyxl")
        df_filtrado = df_xlsx["Setor"] == "Produtos"
        print("\n")
        print(df_xlsx[df_filtrado])
        print("\n")
    elif input_setor == "5":
        df_xlsx = pd.read_excel(r"ferias.xlsx", sheet_name= "pedidos_ao_rh", engine= "openpyxl")
        df_filtrado = df_xlsx["Setor"] == "Operações"
        print("\n")
        print(df_xlsx[df_filtrado])
        print("\n")
    elif input_setor == "6":
        df_xlsx = pd.read_excel(r"ferias.xlsx", sheet_name= "pedidos_ao_rh", engine= "openpyxl")
        df_filtrado = df_xlsx["Setor"] == "Diretoria"
        print("\n")
        print(df_xlsx[df_filtrado])
        print("\n")
    elif input_setor == "7":
        df_xlsx = pd.read_excel(r"ferias.xlsx", sheet_name= "pedidos_ao_rh", engine= "openpyxl")
        df_filtrado = df_xlsx["Setor"] == "Facilities"
        print("\n")
        print(df_xlsx[df_filtrado])
        print("\n")
    elif input_setor <"1" or input_setor >"7":
        print("\n")
        print("Digite uma opção correta, de 1 á 7 !!!")
        print("\n")
    
    
    #Final da função, chama as opções para retornos:
    final = input("Digite 1 para retornar ao menu, 2 para entrar com um novo pedido, ou qualquer tecla para encerrar: ")

    if final == "1":
        python = sys.executable
        os.execl(python,python, * sys.argv)
    elif final == "2":
        novo_pedido()
    else:
        print("Obrigado e até mais!")
        exit()

#abrir e visualizar os feriados nacionais, e depois dar a opção de gravar um pedido, voltar ao menu ou sair.
def feriados_nacionais(): #concluído
    print("\n")
    print("Verifique abaixo os feriados nacionais.\nLembre-se: Férias não podem começar nos dias:")
    print("\n")
    print("DSR - DescansoSemanal Remunerado\n2 dias que antecedem o DSR (quinta ou sexta-feira)\nFeriados Nacionais")
    print("\n")
    df_xlsx = pd.read_excel("ferias.xlsx", sheet_name= "feriados_nacionais")
    print(df_xlsx)
    print("\n")

    #Final da função, chama as opções para retornos:
    final = input("Digite 1 para retornar ao menu, 2 para entrar com um novo pedido, ou qualquer tecla para encerrar: ")

    if final == "1":
        python = sys.executable
        os.execl(python,python, * sys.argv)
    elif final == "2":
        novo_pedido()
    else:
        print("Obrigado e até mais!")
        exit()

#incluir ou excluir um pedido

def novo_pedido(): #em andamento
    print("\n")
    print("Área de Pedidos - Digite seus dados e verifique se existe a disponibilidade que você deseja.")
    print("\n")
    input("Digite seu nome completo: ")
    print("Setores disponíveis:\n1 - Marketing\n2 - Tecnologia\n3 - Logística\n4 - Produtos\n5 - Atendimento\n6 - Diretoria\n7 - Facilities")
    input("Digite o número do seu setor: ")
    input("Digite a data de início das férias: ")
    input("Digite a data de encerramento das férias: ")
    #incluir ou excluir, e depois visualizar, e dar a opção de retornar ao menu ou encerrar.


if entrada =="1":
    pedidos_do_setor()
elif entrada == "2":
    feriados_nacionais()
elif entrada == "3":
    novo_pedido()
elif entrada == "4":
    exit()
else:
    print("Você digitou uma opção inválida, o sistema será reiniciado, digite uma opção de 1 á 4 !!!")
    python = sys.executable
    os.execl(python,python, * sys.argv)