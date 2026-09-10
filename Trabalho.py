from tkinter import *
from tkinter import Canvas
from tkinter import ttk

def base_resisitor_valor():
    if valor_da_resistencia.get() != "" and tolerancia_valor.get() != "":
        caixa_resultado.create_rectangle(75, 50, 375, 100, fill="#D2B48C",
                                         outline="#6B3E26", width=2)
        
        caixa_resultado.delete("texto")
    if tolerancia_valor.get() == "Sem cor":
        caixa_resultado.create_text(225, 25, text="Resistor de 3 Faixas", font=("Arial", 15 , "bold"), fill="black", anchor="center", tags="texto")
    else:
        caixa_resultado.create_text(225, 25, text="Resistor de 4 Faixas", font=("Arial", 15 , "bold"), fill="black", anchor="center", tags="texto")

# função alternar
def alternar_radiobutton():
    if opcao.get() == 1:
        frame_valor.lift()
    else:
        frame_cores.lift()

# Criando a janela
janela = Tk()
janela.title("SAPZ - Calculadora de Códigos de Cores de Resistores")
janela.geometry("570x480")
janela.configure(bg="#D3D3D3")
janela.resizable(False, False)

canvas = Canvas(janela, width = 510,
                height = 410, bg="white",
                highlightthickness=2, highlightcolor="#D3D3D3")
canvas.pack(pady=(55, 10), padx=10)

# Criando o titulo
Label(janela, text="Calculadora de Resistor",
      font=("Arial", 15, "bold"),
      bg="#D3D3D3"
      ).place(x=25, y=15)

# Criando o titulo de baixo
Label(janela, text="Como Deseja Informar o Resistor", 
      font=("Arial", 8, "bold"), bg="white"
      ).place(x=35, y=65)

# Criando os checkbuttons
opcao = IntVar(value=1)

radiobutton_valor = Radiobutton(text="Valor da Resistência",
                                font=("Arial", 7, "bold"), variable=opcao, 
                                value=1, command=alternar_radiobutton,
                                bg="#D3D3D3")
radiobutton_valor.place(x=35, y=90)

radiobutton_cores = Radiobutton(text="Cores do resistor",
                                font=("Arial", 7, "bold"), variable=opcao,
                                value=2, command=alternar_radiobutton, 
                                bg="#D3D3D3")
radiobutton_cores.place(x=165, y=90)

# Fundo branco valor da resistencia
frame_valor = Frame(canvas, bg="white", 
                    width=500, height=410)
frame_valor.place(x=5, y=65)

# Fundo branco cores da resistencia
frame_cores = Frame(canvas, bg="white", 
                    width=500, height=410)
frame_cores.place(x=5, y=65)

# Itens valor da resistencia
Label(frame_valor, text="Valor da Resistência(Ω):",
      font=("Arial", 8)
      ).place(x=5, y=0)

borda_entry_valor = Frame(frame_valor, padx=2,
                          pady=2, bg="#D3D3D3")
borda_entry_valor.place(x=5, y=30)
valor_da_resistencia = Entry(borda_entry_valor, bd=0)
valor_da_resistencia.pack()

Label(frame_valor, text="Tolência:",
      font=("Arial", 8)
      ).place(x=150, y=0)

tolerancia_valor = ttk.Combobox(frame_valor, values=[
                                "Marrom", "Vermelho", "Verde",
                                "Azul", "Violeta", "Cinza",
                                "Dourado", "Prata", "Sem cor"
                                ],font=("Arial", 8, "bold"),
                                state="readonly")
tolerancia_valor.place(x=150, y=30)

borda_botao_calcular = Frame(frame_valor, padx=2,
                             pady=2, bg="#D3D3D3")
borda_botao_calcular.place(x=5, y=60)

botao_calcular_cores = Button(borda_botao_calcular, text="Calcular cores",
                              font=("Arial", 8, "bold"), bg="#3F9C8F",
                              fg="white", bd=0, command=base_resisitor_valor)
botao_calcular_cores.pack()

Label(frame_valor, text="Digite o valor da resistência ou selecone as cores",
      font=("Arial", 8, "bold")
      ).place(x=5, y=90)

# Caixa do resistor valor
borda_caixa_resultado = Frame(frame_valor, padx=3,
                              pady=3, bg="#D3D3D3")
borda_caixa_resultado.place(x=10, y=120)
caixa_resultado = Canvas(borda_caixa_resultado, bg="#E0E0E0",
                        width=475, height=170)
caixa_resultado.pack()

# Itens cores da resistencia
Label(frame_cores, text=("Banda 1:"),
      font=("Arial", 8)
      ).place(x=10, y=0)

banda_1 = ttk.Combobox(frame_cores, values=[
                       "Preto", "Marrom", "Vermelho",
                       "Laranja", "Amarelo", "Verde",
                       "Azul", "Violeta", "Cinza", "Branco"
                       ], font=("Arial", 8, "bold"),
                       state="readonly", width=15)
banda_1.place(x=10, y=30)

Label(frame_cores, text=("Banda 2:"),
      font=("Arial", 8)
      ).place(x=135, y=0)

banda_2 = ttk.Combobox(frame_cores, values=[
                       "Preto", "Marrom", "Vermelho",
                       "Laranja", "Amarelo", "Verde",
                       "Azul", "Violeta", "Cinza", "Branco"
                       ], font=("Arial", 8, "bold"),
                       state="readonly", width=15)
banda_2.place(x=135, y=30)

Label(frame_cores, text=("Multiplicador:"),
      font=("Arial", 8)
      ).place(x=260, y=0)

multiplicador = ttk.Combobox(frame_cores, values=[
                             "Preto", "Marrom", "Vermelho",
                             "Laranja", "Amarelo", "Verde",
                             "Azul", "Violeta", "Cinza", "Branco",
                             "Dourado", "Prata"
                             ], font=("Arial", 8, "bold"),
                             state="readonly", width=15)
multiplicador.place(x=260, y=30)

Label(frame_cores, text=("Tolerância:"),
      font=("Arial", 8)
      ).place(x=385, y=0)

tolerancia_cores = ttk.Combobox(frame_cores, values=[
                                "Marrom", "Vermelho", "Verde",
                                "Azul", "Violeta", "Cinza",
                                "Dourado", "Prata", "Sem cor"
                                ], font=("Arial", 8, "bold"),
                                state="readonly", width=15)
tolerancia_cores.place(x=385, y=30)

borda_botao_calcular = Frame(frame_cores, padx=2,
                             pady=2, bg="#D3D3D3")
borda_botao_calcular.place(x=5, y=60)

botao_calcular_resistencia = Button(borda_botao_calcular, text="Calcular resistência",
                                    font=("Arial", 8, "bold"), bg="#3F9C8F",
                                    fg="white", bd=0)
botao_calcular_resistencia.pack()

resultado_resistencia = Label(frame_cores, text="Digite o valor da resistência ou selecone as cores",
                              font=("Arial", 8, "bold"))
resultado_resistencia.place(x=5, y=90)

# Caixa do resistor cores
borda_caixa_resultado = Frame(frame_cores, padx=3, pady=3, bg="#D3D3D3")
borda_caixa_resultado.place(x=10, y=120)
caixa_resultado_2 = Canvas(borda_caixa_resultado, bg="#E0E0E0",
                          width=475, height=170)
caixa_resultado_2.pack()

frame_valor.lift()
janela.mainloop()