from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from cgitb import text

from tkcalendar import DateEntry  # Importando o calendario

from view import *  # Importando os View

############### CORES ###############
cor0 = "#F0F3F5"  # Preto
cor1 = "#FEFFFF"  # Branco
cor2 = "#4FA882"  # Verde
cor3 = "#38576B"  # Valor
cor4 = "#403D3D"  # Letra
cor5 = "#E06636"  # Profit
cor6 = "#036CFC"  # Azul
cor7 = "#EF5350"  # Vermelho
cor8 = "#263238"  # + Verde
cor9 = "#E9EDF5"  # SkyBlue
cor10 = "#E0FFFF"  # Light Cyan

############### Criando Janela ###############
janela = Tk()
janela.title("Controle de Viagem")
janela.geometry('1043x560')
janela.configure(bg=cor9)
janela.resizable(width=FALSE, height=FALSE)

############### Dividindo Janela ###############
frame_cima = Frame(janela, width=310, height=30, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=0)

frame_meio = Frame(janela, width=310, height=303, bg=cor10, relief='flat')
frame_meio.grid(row=1, column=0, padx=0, pady=0)

frame_baixo = Frame(janela, width=310, height=153, bg=cor7, relief='flat')
frame_baixo.grid(row=2, column=0, padx=1, pady=0)

frame_cima_direita = Frame(janela, width=588, height=30, bg=cor2, relief='flat')
frame_cima_direita.grid(row=0, column=1, padx=0, pady=0)

frame_direita = Frame(janela, width=588, height=403, bg=cor1, relief='flat')
frame_direita.grid(row=1, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

############### Label Cima ###############
app_nome = Label(frame_cima, text='Informações da Viagem', anchor=NW, font=('Ivy 13 bold'), bg=cor2, fg=cor1,
                 relief='flat')
app_nome.place(x=10, y=5)

############### Label Cima Direita ###############
app_nome = Label(frame_cima_direita, text='Tabela de Viajens', anchor=NW, font=('Ivy 13 bold'), bg=cor2, fg=cor1,
                 relief='flat')
app_nome.place(x=10, y=5)


# Função Inserir
def inserir():
    data = e_data.get
    calculo = e_calculo.get
    kmInicial = e_km_i.get
    kmFinal = e_km_f.get
    kmMorto = e_km_m.get
    kmRodado = e_km_r.get
    peso = e_peso.get
    entCol = e_ent_col.get
    disel = e_dissel.get
    manutencao = e_manutencao.get
    ganhos = e_ganhos.get
    gastos = e_gastos.get
    saldo = e_saldo.get

    lista = [data, calculo, kmInicial, kmFinal, kmMorto, kmRodado, peso, entCol, disel, manutencao, ganhos, gastos,
             saldo]

    if kmInicial=='':
        messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        e_data.delete(0, 'end')
        e_calculo.delete(0, 'end')
        e_km_i.delete(0, 'end')
        e_km_f.delete(0, 'end')
        e_km_m.delete(0, 'end')
        e_km_r.delete(0, 'end')
        e_peso.delete(0, 'end')
        e_ent_col.delete(0, 'end')
        e_dissel.delete(0, 'end')
        e_manutencao.delete(0, 'end')
        e_ganhos.delete(0, 'end')
        e_gastos.delete(0, 'end')
        e_saldo.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()


############### Configurando Label Baixo ###############
# Data da Viajem
l_data = Label(frame_meio, text='Data da Viajem *', anchor=NW, font=('Ivy 10 bold'), bg=cor10, fg=cor4, relief='flat')
l_data.place(x=10, y=5)
e_data = DateEntry(frame_meio, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022,
                   locale='pt_BR')
e_data.place(x=15, y=30)
# Estado
l_calculo = Label(frame_meio, text='Tabela de calculo *', anchor=NW, font=('Ivy 10 bold'), bg=cor10, fg=cor4,
                  relief='flat')
l_calculo.place(x=160, y=5)
e_calculo = Entry(frame_meio, width=20, justify='left', relief='solid')
e_calculo.place(x=165, y=30)

# Km Inicial
l_km_i = Label(frame_meio, text='Km Inicial *', anchor=NW, font=('Ivy 10 bold'), bg=cor10, fg=cor4, relief='flat')
l_km_i.place(x=10, y=55)
e_km_i = Entry(frame_meio, width=45, justify='left', relief='solid')
e_km_i.place(x=15, y=80)
# Km Final
l_km_f = Label(frame_meio, text='Km Final *', anchor=NW, font=('Ivy 10 bold'), bg=cor10, fg=cor4, relief='flat')
l_km_f.place(x=10, y=105)
e_km_f = Entry(frame_meio, width=45, justify='left', relief='solid')
e_km_f.place(x=15, y=130)
# Km Morto
l_km_m = Label(frame_meio, text='Km Morto *', anchor=NW, font=('Ivy 10 bold'), bg=cor10, fg=cor4, relief='flat')
l_km_m.place(x=10, y=155)
e_km_m = Entry(frame_meio, width=45, justify='left', relief='solid')
e_km_m.place(x=15, y=180)
# Km Rodado
l_km_r = Label(frame_meio, text='Km Rodado *', anchor=NW, font=('Ivy 10 bold'), bg=cor10, fg=cor4, relief='flat')
l_km_r.place(x=10, y=205)
e_km_r = Entry(frame_meio, width=45, justify='left', relief='solid')
e_km_r.place(x=15, y=230)
# Peso
l_peso = Label(frame_meio, text='Peso * - KG', anchor=NW, font=('Ivy 10 bold'), bg=cor10, fg=cor4, relief='flat')
l_peso.place(x=10, y=255)
e_peso = Entry(frame_meio, width=14, justify='left', relief='solid')
e_peso.place(x=15, y=280)
# Km Ent/Col
l_ent_col = Label(frame_meio, text='Ent/Col *', anchor=NW, font=('Ivy 10 bold'), bg=cor10, fg=cor4, relief='flat')
l_ent_col.place(x=115, y=255)
e_ent_col = Entry(frame_meio, width=10, justify='left', relief='solid')
e_ent_col.place(x=120, y=280)
# Dissel
l_dissel = Label(frame_meio, text='Dissel *', anchor=NW, font=('Ivy 10 bold'), bg=cor10, fg=cor4, relief='flat')
l_dissel.place(x=200, y=255)
e_dissel = Entry(frame_meio, width=13, justify='left', relief='solid')
e_dissel.place(x=205, y=280)

# Manutenção
l_manutencao = Label(frame_baixo, text='Manutenção', anchor=NW, font=('Ivy 10 bold'), bg=cor7, fg=cor4, relief='flat')
l_manutencao.place(x=10, y=5)
e_manutencao = Entry(frame_baixo, width=22, justify='left', relief='solid')
e_manutencao.place(x=15, y=30)
# Total Ganhos
l_ganhos = Label(frame_baixo, text='Ganhos', anchor=NW, font=('Ivy 10 bold'), bg=cor7, fg=cor4, relief='flat')
l_ganhos.place(x=160, y=5)
e_ganhos = Entry(frame_baixo, width=22, justify='left', relief='solid')
e_ganhos.place(x=165, y=30)
# Total Gastos
l_gastos = Label(frame_baixo, text='Gastos', anchor=NW, font=('Ivy 10 bold'), bg=cor7, fg=cor4, relief='flat')
l_gastos.place(x=10, y=55)
e_gastos = Entry(frame_baixo, width=22, justify='left', relief='solid')
e_gastos.place(x=15, y=80)
# Saldo
l_saldo = Label(frame_baixo, text='Saldo', anchor=NW, font=('Ivy 10 bold'), bg=cor7, fg=cor4, relief='flat')
l_saldo.place(x=160, y=55)
e_saldo = Entry(frame_baixo, width=22, justify='left', relief='solid')
e_saldo.place(x=165, y=80)

# Bt_Inserir
bt_inserir = Button(frame_baixo, text='Inserir', command=inserir, width=10, font=('Ivy 9 bold'), bg=cor6, fg=cor1,
                    relief='raised', overrelief='ridge')
bt_inserir.place(x=10, y=115)
# Bt_Atualizar
bt_atualizar = Button(frame_baixo, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=cor2, fg=cor1, relief='raised',
                      overrelief='ridge')
bt_atualizar.place(x=105, y=115)
# Bt_Deletar
bt_deletar = Button(frame_baixo, text='Deletar', width=10, font=('Ivy 9 bold'), bg=cor7, fg=cor1, relief='raised',
                    overrelief='ridge')
bt_deletar.place(x=200, y=115)


################ Codigo para tabela ####################

def mostrar():
    lista = mostrar_info()

    # lista para cabecario
    tabela_head = ['ID', 'Data', 'Calculo', 'Km Inicial', 'Km Final', 'Km Morto', 'Km Rodado', 'Peso', 'Ent/Col',
                   'Dissel', 'Manutenção', 'Ganhos', 'Gastos', 'Saldo']

    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center", "nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 100, 120, 50, 100, 30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)


# Chamndo a Função Mostrar
mostrar()

janela.mainloop()
