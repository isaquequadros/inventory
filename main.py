from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DataEntry
from datetime import date
from tkinter import messagebox
from tkinter import filedialog as fd


co0 = "#fff"
co1 = "#000"
co2 = "#fff0000"
co3 = "#292929"

#criando a janela
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando Frames

frameCima = Frame(janela, width=1043, height=50, bg=co0, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co0, pady=10, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co0, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)



 
# criando funções ---------------------------------------------------------------
global tree

# Funcao inserir
	def inserir:
		global imagem, imagem_string, l_imagem

		nome = e_nome.get()
		local = e_local.get()
		descricao = e_descricao.get()
		model = e_model.get()
		data = e_cal.get()
		valor = e_valor.get()
		serie = e_serial.get()
		imagem = imagem_string

		lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

		for i in lista_inserir:
			if i =='':
				messagebox.showerror('Erro','Preencha todos os campos')
				return

	inserir_form(lista_inserir)
	messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

		e_nome.delete(0,'end')
		e_local.delete(0,'end')
		e_descricao.delete(0,'end')
		e_model.delete(0,'end')
		e_cal.delete(0,'end')
		e_valor.delete(0,'end')
		e_serial.delete(0,'end')

		for widget in  frameMeio.winfo_children():
			widget.destroy()

			mostrar()

# funcao deletar
def deletar():
	try:
		treey_dados = tree.focus()
		treey_dicionario = tree.item(treey_dados)
		treey_lista = treey_dicionario['values']
		valor = [int(treev_lista[0])]		
		
		deletar_form([valor])

		messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

		mostrar()

	except IndexError:
		messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')



# funcao para escolher imagem
global imagem, imagem_string, l_imagem

def escolher_imagem():
	global imagem, imagem_string, l_imagem	

	imagem = fd.askopenfilename()
	imagem_string = imagem

	# Abrindo imagem
	imagem = Image.open(imagem)
	imagem = imagem.resize((170,170))
	imagem = ImageTk.PhotoImage(imagem)
	l_imagem = Label(frameMeio, image=imagem, bg=co0, fg=co3)
	l_imagem.place(x=700, y=10)

# funcao para ver imagem
def ver_imagem():
	global imagem, imagem_string, l_imagem

	treey_dados = tree.focus()
	treey_dicionario = tree.item(treey_dados)
	treey_lista = treey_dicionario['values']

	valor = [int(treev_lista[0])]

	iten = ver_item(valor)

	print(iten)

	imagem = iten[0][8]

	imagem = Image.open(imagem)
	imagem = imagem.resize((45,45))
	imagem = ImageTk.PhotoImage(imagem)

	l_imagem = Label(frameMeio, image=imagem, bg=co0, fg=co3)
	l_imagem.place(x=7000, y=0)

# FRAME DE CIMA *******************************************************

# Abrindo imagem
app_img = Image.open('inventario.jpg')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Inventario Pessoal ', width=900, compound=LEFT, relief=NW, font=('Verdana 20 bold'), bg=co0, fg=co3)
app_logo.place(x=0, y=0)

# Frame do meio --------------------------------------------------------

# Criando entradas
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text='Sala/Área', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=11)

l_model = Label(frameMeio, text='Marca/Model', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_model.place(x=10, y=100)
e_model = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_model.place(x=130, y=101)

l_cal = Label(frameMeio, text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, background='darkblue', bordewidth=2, year=2022)
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_valor.place(x=10, y=100)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=101)

l_serial = Label(frameMeio, text='Numero de série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serial.place(x=130, y=191)

# botões --------------------------------------------------------
#botões carregar
l_carregar = Label(frameMeio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMeio, command=escolher_imagem, width=29, text='carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co3)
b_carregar.place(x=130, y=220)

#botões inserir
img_add = Image.open('add.png')
img_add = app_img.resize((20,20))
img_add = ImageTk.PhotoImage(app_img)

b_inserir = Button(frameMeio, command=inserir, image=img_add, width=95, text='carregar'.upper(), compound=CENTER, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co3)
b_inserir.place(x=330, y=10)

#botões Atualizar
img_update = Image.open('update.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(frameMeio, command=atualizar, image=img_update, width=95, text='carregar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co3)
b_update.place(x=330, y=50)

#botões Deletar
img_delete = Image.open('delete.png')
img_delete = app_img.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frameMeio, command=deletar, image=img_add, width=95, text='carregar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co3)
b_delete.place(x=330, y=90)

#botões ver imagem
img_item = Image.open('item.png')
img_item = app_img.resize((20,20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(frameMeio, command=ver_imagem, image=img_add, width=95, text='carregar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co0, fg=co3)
b_item.place(x=330, y=221)

# labels quantidade total e valores

l_total = Label(frameMeio, text='', width=14, height=2, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_total.place(x=450, y=17)
l_total = Label(frameMeio, text='Valor Total de todos os itens   ', width=14, height=2, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_total.place(x=450, y=12)

l_qtd = Label(frameMeio, text='', width=14, height=1, pady=5, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co2)
l_qtd.place(x=450, y=130)
l_qtd = Label(frameMeio, text='Quantidade total de itens   ', width=14, height=2, anchor=NW, font=('Ivy 10 bold'), bg=co0, fg=co3)
l_qtd.place(x=450, y=92)

# Tabela
def mostrar():
	global tree

	# creating a treeview with dual scrollbars
	tabela_head = ['#Item', 'Nome', 'Sala/Área', 'Descrição', 'Marca/Modelo', 'Data da compra', 'Valor da compra', 'Numero de série']

	lista_itens = ver_form()

	global Tree

	tree = ttk.Treeview(frameBaixo, selectmode="extended", columns="tabela_head", show='headings')

	# vertical scrollbar
	vsb = ttk.Scrollbar(
		frameBaixo, orient="vertical", command=tree.xview)

	# horizontal scrollbar

	tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

	tree.grid(column=0, row=0, sticky='NSEW')
	vsb.grid(column=1, row=0, sticky='ns')
	hsb.grid(column=0, row=1, sticky='ew')
	frameBaixo.grid_rowconfigure(0, weight=12)

	hd=["center","center","center","center","center","center","center","center",]
	h=[40,150,100,160,130,100,100,100]
	n=0

for col in tabela_head:
	tree.heading(col, text=col.title(), anchor=CENTER)
	# adjust the column's width to the header string
	tree.column(col, width=h[n],anchor=hd[n])
	n+-1

# inserindo os itens dentro da tabela
for item in lista_itens:
	tree.insert('','end', values=item)

quantidade = []
for iten in lista_itens:
	quantidade.append(iten[6])

Total_valor = sum(quantidade)
Total_itens = len(quantidade)

l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
l_qtd['text'] = Total_itens

mostrar()

janela.mainloop()