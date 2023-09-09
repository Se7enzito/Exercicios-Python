from tkinter import *

def cadastrarAluno():
    print(f"Nome: {nome.get()}\nIdade: {idade.get()}\nNota: {nota.get()}")
    nome.delete(0, END)
    idade.delete(0, END)
    nota.delete(0, END)

janela = Tk()
janela.title("Cadastro de Alunos")
janela.geometry("380x200")

tnome = Label(text="Insira o nome do aluno")
nome = Entry()
tidade = Label(text="Insira a idade do aluno")
idade = Entry(validate="key")
tnota = Label(text="Insira a nota do aluno")
nota = Entry(validate="key")

def validate_input(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False
    
enviar = Button(janela, text="Cadastrar", command=cadastrarAluno)

validate_func = janela.register(validate_input)
idade.config(validate="key", validatecommand=(validate_func, "%P"))
nota.config(validate="key", validatecommand=(validate_func, "%P"))

tnome.grid(row=0, column=0)
tidade.grid(row=0, column=1)
tnota.grid(row=0, column=2)
nome.grid(row=1, column=0)
idade.grid(row=1, column=1)
nota.grid(row=1, column=2)
enviar.grid(row=2, column=1)

janela.mainloop()