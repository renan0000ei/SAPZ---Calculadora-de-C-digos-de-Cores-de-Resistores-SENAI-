from tkinter import *
from tkinter import Canvas
from tkinter import ttk

# Criando a janela
def alternar_radiobutton():
    if opcao.get() == 1:
        frame_valor.lift()
    else:
        frame_cores.lift()


janela = Tk()
janela.title("SAPZ - Calculadora de Códigos de Cores de Resistores")
janela.geometry("500x500")
janela.configure(bg="#D3D3D3")
janela.resizable(False, False)

canvas = Canvas(janela, width = 450,
                 height = 410, bg="white",
                 highlightthickness=2, highlightcolor="#D3D3D3")
canvas.pack(pady=(55, 10))

# Criando o titulo
Label(janela, text="Calculadora de Resistor",
       font=("Arial", 15, "bold"),
       bg="#D3D3D3"
       ).place(x=25, y=15)

# Criando o titulo de baixo
Label(janela, text="Como Deseja Informar o Resistor", 
      font=("Arial", 8, "bold"), bg="white"
      ).place(x=30, y=65)

# Criando os checkbuttons
opcao = IntVar(value=1)

radiobutton_valor = Radiobutton(text="Valor da Resistência",
                                    font=("Arial", 7, "bold"), variable=opcao, 
                                    value=1, command=alternar_radiobutton,
                                    bg="#D3D3D3")
radiobutton_valor.place(x=30, y=90)

radiobutton_cores = Radiobutton(text="Valor da Resistência",
                                 font=("Arial", 7, "bold"), variable=opcao,
                                 value=2, command=alternar_radiobutton, 
                                 bg="#D3D3D3")
radiobutton_cores.place(x=165, y=90)

# Fundo branco valor da resistencia
frame_valor = Frame(canvas, bg="white", width=450, height=410)
frame_valor.place(x=5, y=65)

# Fundo branco cores da resistencia
frame_cores = Frame(canvas, bg="white", width=450, height=410)
frame_cores.place(x=5, y=65)

# Itens valor da resistencia
Label(frame_valor, text="Valor da Resistência(Ω):",
      font=("Arial", 8, "bold"), bg="white"
      ).place(x=5, y=0)

borda_entry_valor = Frame(frame_valor, padx=2, pady=2, bg="#D3D3D3")
borda_entry_valor.place(x=5, y=30)
valor_da_resistencia = Entry(borda_entry_valor, bd=0)
valor_da_resistencia.pack()

Label(frame_valor, text="Tolência:", font=("Arial", 8, "bold"), bg="white").place(x=150, y=0)

tolerancia = ttk.Combobox(frame_valor, values=["Marrom", "Vermelho", "Verde", "Azul", "Violeta", "Cinza", "Dourado", "Prata", "Sem cor"], font=("Arial", 8, "bold"),
                          state="readonly")
tolerancia.place(x=150, y=30)

borda_botao_calcular = Frame(frame_valor, padx=2, pady=2, bg="#D3D3D3")
borda_botao_calcular.place(x=5, y=60)
botao_calcular_cores = Button(borda_botao_calcular, text="Calcular cores", font=("Arial", 8, "bold"), bg="#3F9C8F", fg="white", bd=0)
botao_calcular_cores.pack()

Label(frame_valor, text="Digite o valor da resistência ou selecone as cores", font=("Arial", 8, "bold")).place(x=5, y=90)

# Caixa do resistor
caixa_resultado = Frame(
    frame_valor,
    bg="white",
    width=405,
    height=155,
    bd=1, relief="ridge")
caixa_resultado.place(x=25, y=150)




frame_valor.lift()
janela.mainloop()