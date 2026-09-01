from tkinter import *
from tkinter import Canvas

# Criando a janela

def alternar_radiobutton():
    if opcao.get() == 1:
        frame_valor.lift()
    else:
        frame_cores.lift()


janela = Tk()
janela.title("SAPZ - Calculadora de Códigos de Cores de Resistores")
janela.geometry("500x400")
janela.configure(bg="#D3D3D3")
janela.resizable(False, False)

canvas = Canvas(janela, width = 450,
                 height = 380, bg="white")
canvas.pack(pady=(55, 10))

# Criando o titulo

Label(janela, text="Calculadora de Resistor",
       font=("Arial", 15),
       bg="#D3D3D3"
       ).place(x=25, y=15)

# Criando o titulo de baixo

Label(janela, text="Como Deseja Informar o Resistor", 
      font=("Arial", 8), bg="white"
      ).place(x=30, y=65)

# Criando os checkbuttons

opcao = IntVar(value=1)

valor_da_resistencia = Radiobutton(text="Valor da Resistência",
                                    font=("Arial", 7), variable=opcao, 
                                    value=1, command=alternar_radiobutton)
valor_da_resistencia.place(x=30, y=90)

cores_do_resistor = Radiobutton(text="Valor da Resistência",
                                 font=("Arial", 7), variable=opcao,
                                 value=2, command=alternar_radiobutton)
cores_do_resistor.place(x=150, y=90)

# Checkbutton valor da resistencia
frame_valor = Frame(canvas, bg="white", width=400, height=200)
frame_valor.place(x=10, y=65)

Label(frame_valor, text="Valor da Resistência(Ω)",
      font=("Arial", 8), bg="white"
      ).place(x=5, y=5)

frame_cores = Frame(canvas, bg="white", width=410, height=200)
frame_cores.place(x=15, y=75)

janela.mainloop()