import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3
import re

#começar com tela com um botão e um entry (nome)- v1
#adicionar mais duas entrys (cpf e estado) e suas labels - v2
#mudar o fundo para uma imagem mais bonita, adicionar readme.txt explicando como usar - v3
#adicionar clicar no botão salva os 3 dados em um sqlite - v4
#Criar uma branch em que le um config.txt com uma lista de 5 estados possiveis separados por pular linha - x1
#Mudar o separador para ; e adicionar mais 5 estados - x2
#Voltar para main, criar outra branch e criar um dropdown com 3 opções (clt, mei, socio) - y1
#Voltar para main, Corrigir o bug da função de cpf - v5
#Merge de x com v - v6
#Adicionar verificação de CPF e de estado, com base na função cpf e na lista de estados .txt antes de adicionar no sqlite v7

#Cria conexção
connection = sqlite3.connect("teste.db")

#Cria o cursos e cria a tabela
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado TEXT)")

with open('config.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    elementos = conteudo.strip().split(';')

def verificar_cpf(cpf):
    padrao = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')
    if padrao.match(cpf):
        return True
    else:
        return False

def inserevalores():
    #Insere linha na tabela
    if estado.get() not in elementos:
        return
    valor = cpf.get()
    if not verificar_cpf(valor):
        return
    query = '''INSERT INTO Tabela1 VALUES (?,?,?)'''
    cursor.execute(query, (e1.get(), cpf.get(), estado.get()))
    connection.commit()

def pegavalores():
    #Pega valores da tabela
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def funcExemplo():
    print("Exemplo de funcao")
    
def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)

    img = tkinter.PhotoImage(file="fundo.PNG")
    label_fundo = tkinter.Label(root, image=img)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
    
    label = tkinter.Label(root, text="Nome")
    label.pack()

    textoEntrada = tkinter.StringVar()
    global e1
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()

    label_cpf = tkinter.Label(root, text="CPF")
    label_cpf.pack()
    global cpf
    cpf = tkinter.Entry(root)
    cpf.pack()

    label_estado = tkinter.Label(root, text="Estado")
    label_estado.pack()
    global estado
    estado = tkinter.Entry(root)
    estado.pack()
    
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = inserevalores  #alterar para chamar outra função
    test2.pack()

    root.iconify() #Minimiza a tela
    root.update()
    root.deiconify() #Maximiza a tela
    root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs

Main()

connection.close()