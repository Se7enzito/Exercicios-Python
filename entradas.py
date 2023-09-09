from tkinter import *

janela = Tk()
janela.title("Ensinamentos")
janela.geometry("300x300")

entrada1 = Entry()
entrada2 = Entry(font=('Arial', 33), fg='red')

inserir = Button(text="Inserir", command=lambda: entrada1.insert(0, "Inserindo..."))
deleter = Button(text="Deletar", command=lambda: [entrada1.delete(0, END), entrada2.delete(0, END)])
capturar = Button(text="Capturar", command=lambda: [entrada2.delete(0, END), entrada2.insert(0, entrada1.get())])

entrada1.pack()
entrada2.pack()
inserir.pack()
deleter.pack()
capturar.pack()

janela.mainloop()