import tkinter as tk

def calcula_tempo_necessario():
    while True:
        try:
            meta_financeira = float(meta_financeira_entry.get())
            economia_mensal = float(economia_mensal_entry.get())
            tempo_necessario = meta_financeira / economia_mensal
            resultado_label.config(text=f"Para alcançar essa meta, será necessário {tempo_necessario:.1f} meses.")
            break
        except ValueError:
            meta_financeira = meta_financeira_entry.get()
            economia_mensal = economia_mensal_entry.get()
            resultado_label.config(text="Por favor, digite um valor númerico.")
            break

# Cria janela
app = tk.Tk()
app.title("Calculadora de Metas Financeiras")
app.geometry("500x250")
app.resizable(False, False)

# Cria label e a entrda da meta financeira
meta_financeira_label = tk.Label(app, text=" Meta Financeira (R$):")
meta_financeira_label.pack(padx=5, pady=5)
meta_financeira_entry = tk.Entry(app)
meta_financeira_entry.pack(padx=5, pady=5)

# Cria label e a entrada da economia financeira
economia_mensal_label = tk.Label(app, text="Economia Mensal (R$):")
economia_mensal_label.pack(padx=5, pady=5)
economia_mensal_entry = tk.Entry(app)
economia_mensal_entry.pack(padx=5, pady=5)

# Cria o botão de calculo
calcular_botao =tk.Button(app, text="Calcular", command=calcula_tempo_necessario)
calcular_botao.pack(padx=5, pady=5)

# Mostra o resultado
resultado_label = tk.Label(app, text="")
resultado_label.pack(padx=5, pady=5)

app.mainloop()

# Recebe a meta
def define_meta_financeira():
    meta_financeira = float(input("Digite o valor da meta financeira: R$"))
    return meta_financeira

# Recebe a economia pretendida
def define_economia_mensal():
    economia_mensal = float(input("Digite o valor que você pretende economizar mensalmente: R$"))
    return economia_mensal

# Calcula o tempo necessário
def calcula_tempo_necessario(meta_financeira, economia_mensal):
    tempo_necessario = meta_financeira / economia_mensal
    return tempo_necessario

# Mostra o resultado
def mostra_resultado(tempo_necessario):
    print(f"Para alcançar essa meta, será necessário {tempo_necessario:.1f} meses.")

def main():
    print("Calculadora de Metas Financeiras")
    meta_financeira = define_meta_financeira()
    economia_mensal = define_economia_mensal()
    tempo_necessario = calcula_tempo_necessario(meta_financeira, economia_mensal)
    mostra_resultado(tempo_necessario)
