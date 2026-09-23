#importando os itens do tkinter
from tkinter import *
from tkinter import Canvas
from tkinter import ttk

#Função que calula a resistencia escolhida pelo usuario e define as cores do resistor
def calcular_resistencia_frame_valor():
      cores = {
      0: "Preto",
      1: "Marrom",
      2: "Vermelho",
      3: "Laranja",
      4: "Amarelo",
      5: "Verde",
      6: "Azul",
      7: "Violeta",
      8: "Cinza",
      9: "Branco"
      }

      multiplicadores = {
      0: "Preto",
      1: "Marrom",
      2: "Vermelho",
      3: "Laranja",
      4: "Amarelo",
      5: "Verde",
      6: "Azul",
      7: "Violeta",
      8: "Cinza",
      9: "Branco",
      -1: "Dourado",
      -2: "Prata"
      }

      valor = float(valor_da_resistencia.get())

      expoente = 0

      while valor >= 100:
        valor = valor / 10
        expoente = expoente + 1

      while valor < 10:
        valor = valor * 10
        expoente = expoente - 1

      if valor % 1 != 0:
        mensagem_valor.config(text="Valor não pode ser representado com 4 faixas")

      digito1 = int(valor // 10)
      digito2 = int(valor % 10)

      global cor_1
      global cor_2
      global cor_3
      global cor_4

      cor_1 = cores[digito1]
      cor_2 = cores[digito2]
      cor_3 = multiplicadores[expoente]
      cor_4 = tolerancia_valor.get()

#Função que calcula as cores escolhidas pelo usuario e define a resistencia do resistor       
def calcular_reisitencia_frame_cor ():
      valores = {
        "Preto": 0,
        "Marrom": 1,
        "Vermelho": 2,
        "Laranja": 3,
        "Amarelo": 4,
        "Verde": 5,
        "Azul": 6,
        "Violeta": 7,
        "Cinza": 8,
        "Branco": 9
      }

      multiplicadores_valores = {
        "Preto": 1,
        "Marrom": 10,
        "Vermelho": 100,
        "Laranja": 1000,
        "Amarelo": 10000,
        "Verde": 100000,
        "Azul": 1000000,
        "Violeta": 10000000,
        "Cinza": 100000000,
        "Branco": 1000000000,
        "Dourado": 0.1,
        "Prata": 0.01
      }

      tolerancias_valores = {
        "Marrom": 1,
        "Vermelho": 2,
        "Verde": 0.5,
        "Azul": 0.25,
        "Violeta": 0.1,
        "Cinza": 0.05,
        "Dourado": 5,
        "Prata": 10,
        "Sem cor": 20
      }

      valor1 = valores[banda_1.get()]
      valor2 = valores[banda_2.get()]
      fator = multiplicadores_valores[multiplicador.get()]
      tolerancia_resultado_cores = tolerancias_valores[tolerancia_cores.get()]
      
      valor = float(valor1 * 10 + valor2) * fator

      if valor >= 1000000000:
            valor_exibicao = valor / 1000000000
            unidade = "GΩ"
      elif valor >= 1000000:
            valor_exibicao = valor / 1000000
            unidade = "MΩ"
      elif valor >= 1000:
            valor_exibicao = valor / 1000
            unidade = "kΩ"
      else:
            valor_exibicao = valor
            unidade = "Ω"

      resultado_resistencia.config(text=f"Resistência: {valor_exibicao:.2f} {unidade} ±{tolerancia_resultado_cores}%"
)

#Função que junta as funções do frame de valor da resistencia para ser usada no botao calcular cores
def valor():
    calcular_resistencia_frame_valor()
    base_resisitor_valor()
    montar_cores_resistor_valor()

#Função que junta as funções do frame de cores da resistencia para ser usada no botao calcular resistencia
def cores():
    base_resistor_cores()
    montar_cores_resistor()
    calcular_reisitencia_frame_cor()

#Função que recebe o nome da cor e retorna o "#" da cor para ser usada no resistor
def receber_cores(nome):
      cores = {
            "Preto": "#000000",
            "Marrom": "#8B4513",
            "Vermelho": "#FF0000",
            "Laranja": "#FFA500",
            "Amarelo": "#FFFF00",
            "Verde": "#008000",
            "Azul": "#0000FF",
            "Violeta": "#800080",
            "Cinza": "#808080",
            "Branco": "#FFFFFF",
            "Dourado": "#FFD700",
            "Prata": "#C0C0C0"
      }
      return cores.get(nome)

#Função que monta as cores na base do resistor no frame valor
def montar_cores_resistor_valor():
    if valor_da_resistencia.get() != "" and tolerancia_valor.get() != "":
        denovo_cor1 = receber_cores(cor_1)
        denovo_cor2 = receber_cores(cor_2)
        denovo_cor3 = receber_cores(cor_3)

        caixa_resultado.create_rectangle(85, 50, 125, 100, fill=denovo_cor1)
        caixa_resultado.create_rectangle(150, 50, 190, 100, fill=denovo_cor2)
        caixa_resultado.create_rectangle(215, 50, 255, 100, fill=denovo_cor3)

        if tolerancia_valor.get() != "Sem cor":
            denovo_cor4 = receber_cores(cor_4)
            caixa_resultado.create_rectangle(280, 50, 320, 100, fill=denovo_cor4)

#Função que monta as cores na base do resistor no frame cores
def montar_cores_resistor():
      cor1 = receber_cores(banda_1.get())
      cor2 = receber_cores(banda_2.get())
      cor3 = receber_cores(multiplicador.get())
      cor4 = receber_cores(tolerancia_cores.get())

      if banda_1.get() != "" and banda_2.get() != "" and multiplicador.get() != "":
          caixa_resultado_2.create_rectangle(85, 50, 125, 100, fill=cor1)
          caixa_resultado_2.create_rectangle(150, 50, 190, 100, fill=cor2)
          caixa_resultado_2.create_rectangle(215, 50, 255, 100, fill=cor3)
      if tolerancia_cores.get() != "Sem cor":
          caixa_resultado_2.create_rectangle(280, 50, 320, 100, fill=cor4)


#Função que cria a base do resistor no frame cores
def base_resistor_cores():
    if banda_1.get() != "" and banda_2.get() != "" and multiplicador.get() != "" and tolerancia_cores != "":
       caixa_resultado_2.create_rectangle(75, 50, 375, 100, fill="#D2B48C",
                                           outline="#6B3E26", width=2)
       caixa_resultado_2.create_rectangle(1, 72, 75, 78, fill="#555555")
       caixa_resultado_2.create_rectangle(375, 72, 450 , 78, fill="#555555")

       caixa_resultado_2.delete("texto")
    if tolerancia_cores.get() == "Sem cor":
         caixa_resultado_2.create_text(225, 25, text="Resistor de 3 Faixas",
                                        font=("Arial", 15 , "bold"), fill="black",
                                        anchor="center", tags="texto")
    else:
         caixa_resultado_2.create_text(225, 25, text="Resistor de 4 Faixas",
                                        font=("Arial", 15 , "bold"), fill="black",
                                        anchor="center", tags="texto")

#Função que cria a base do resistor no frame valor
def base_resisitor_valor():
    if valor_da_resistencia.get() != "" and tolerancia_valor.get() != "":
        caixa_resultado.create_rectangle(75, 50, 375, 100, fill="#D2B48C",
                                         outline="#6B3E26", width=2)
        caixa_resultado.create_rectangle(1, 72, 75, 78, fill="#555555")
        caixa_resultado.create_rectangle(375, 72, 450 , 78, fill="#555555")
        
        caixa_resultado.delete("texto")
    if tolerancia_valor.get() == "Sem cor":
        caixa_resultado.create_text(225, 25, text="Resistor de 3 Faixas",
                                       font=("Arial", 15 , "bold"), fill="black",
                                       anchor="center", tags="texto")
    else:
        caixa_resultado.create_text(225, 25, text="Resistor de 4 Faixas",
                                       font=("Arial", 15 , "bold"), fill="black",
                                       anchor="center", tags="texto")

# função alternar frame
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

# Fundo branco(frame) valor da resistencia
frame_valor = Frame(canvas, bg="white", 
                    width=500, height=400)
frame_valor.place(x=5, y=65)

# Fundo branco(frame) cores da resistencia
frame_cores = Frame(canvas, bg="white", 
                    width=500, height=400)
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
                              fg="white", bd=0, command=valor)
botao_calcular_cores.pack()

mensagem_valor = Label(frame_valor, text="Digite o valor da resistência ou selecone as cores",
                        font=("Arial", 8, "bold"))
mensagem_valor.place(x=5, y=90)

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
                                    fg="white", bd=0, command=cores)
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