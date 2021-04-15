from tkinter import messagebox
from tkinter import *
def show_frame(page_name):
  '''Show a frame for the given page name'''
  frame = frames[page_name]
  frame.tkraise()
app = Tk()
app.geometry("1024x768")
top = Frame(app)
top.pack(side="top", fill="both", expand=True)
top.grid_rowconfigure(0, weight=1)
top.grid_columnconfigure(0, weight=1)
frames = {}
#COMANDOS
def ir_para_adicionar():
  show_frame("PageOne")
def ir_para_remover():
  show_frame("PageTwo")
page_name = "StartPage"
frame = Frame(top)
frames[page_name] = frame
frame.grid(row=0, column=0, sticky="nsew")
label = Label(frame, text = "Teoria Grafos", pady = 10)
label.pack()
adicionar = Button(frame, text = "Iniciar o Grafo", command = ir_para_adicionar,)
adicionar.pack()
remover = Button(frame, text = "SAIR", command = ir_para_remover)
remover.pack()
#ADICIONAR PRODUTO
def ir_para_adicionar_cerveja():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

def ir_para_adicionar_destilados():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

def ir_para_adicionar_refrigerante():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

def ir_para_adicionar_outros():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

def ir_para_adicionar_voltar():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

page_name = "PageOne"
frame = Frame(top)
frames[page_name] = frame
frame.grid(row=0, column=0, sticky="nsew")

label = Label(frame, text = "ADICIONAR PRODUTO")
label.pack(side = TOP)

adicionar_cerveja = Button(frame, text = "CERVEJA", command = ir_para_adicionar_cerveja)
adicionar_cerveja.pack()
adicionar_destilados = Button(frame, text = "REFRIGERANTE", command = ir_para_adicionar_destilados)
adicionar_destilados.pack()
adicionar_refrigerante = Button(frame, text = "DESTILADOS", command = ir_para_adicionar_refrigerante)
adicionar_refrigerante.pack()
adicionar_voltar = Button(frame, text = "SAIR", command = ir_para_adicionar_voltar)
adicionar_voltar.pack()

#REMOVER PRODUTO
def ir_para_remover_cerveja():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

def ir_para_remover_destilados():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

def ir_para_remover_refrigerante():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

def ir_para_remover_outros():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

def ir_para_remover_voltar():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

page_name = "PageTwo"
frame = Frame(top)
frames[page_name] = frame
frame.grid(row=0, column=0, sticky="nsew")

label = Label(frame, text = "REMOVER PRODUTO")
label.pack(side = TOP)

remover_cerveja = Button(frame, text = "CERVEJA", command = ir_para_remover_cerveja)
remover_cerveja.pack()
remover_destilados = Button(frame, text = "REFRIGERANTE", command = ir_para_remover_destilados)
remover_destilados.pack()
remover_refrigerante = Button(frame, text = "REFRIGERANTE", command = ir_para_remover_refrigerante)
remover_refrigerante.pack()
remover_outros = Entry(frame, text = "")
remover_outros.pack()
remover_voltar = Button(frame, text = "SAIR", command = ir_para_remover_voltar)
remover_voltar.pack()

'''
#QUANTIDADE
def ir_para_quantidade():
  msg = messagebox.showinfo( "Hello Python", "Hello World")

frame_quantidade = Frame(top)

label = Label(frame_quantidade, text = "QUANTIDADE")
label.pack(side = TOP)

quantidade = Entry(frame_quantidade, text = "")
quantidade.pack(side = BOTTOM)
'''

show_frame("StartPage")
app.mainloop()

