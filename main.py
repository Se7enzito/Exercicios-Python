from tkinter import *
from playsound import playsound

def delEntry():
    entrada.delete(0, END)

def imprimirSaudacao():
    print(f"Seja bem-vindo {entrada.get()} como estão seus estudos?")
    delEntry()

janela = Tk()
# janela.geometry("300x300")
# janela.resizable(False, False)

# legenda1 = Label(text="Aperte o botão", fg="white", bg="black", font=("Arial", 23))
legenda1 = Label(text="Aperte o botão")
# legenda1.pack()
legenda1.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

entrada = Entry(fg="white", bg="black")
# entrada.pack(padx=10, pady=5)
entrada.grid(row=1, column=0, padx=10, pady=5)

enviar = Button(janela, text="Enviar", command=imprimirSaudacao)
# enviar.pack(padx=10, pady=5)
enviar.grid(row=1, column=1, padx=10, pady=5)

# botao_larissa_pix = Button(text="Larissa Pedindo Pix", padx="12", pady="12", command=lambda: playsound("larissa-manoel-pedindo-pix.mp3"))
# botao_larissa_pix.pack()

janela.mainloop()