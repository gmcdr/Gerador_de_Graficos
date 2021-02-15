from tkinter import *
import matplotlib.pyplot as plt

x = []
y = []
janela = Tk()
janela.title('Gerador de Gráfico')
janela["background"] = "#565656"
janela.iconbitmap("imagens/imagen.ico")
#Funções
#------------------------------------------------------------------------------
def bt_click():
    t1 = len(x)
    t2 = len(y)
    if t1 != t2:
        y.clear() ; x.clear()
        error  = Tk()
        error.title('Error !')
        error.iconbitmap("imagens/error.ico")
        lb3 = Label(error,text='Os tamanhos de X e Y são diferentes, reincira os valores !')
        lb3.place(x=15,y=30)
        error.geometry('330x70+200+200')
        error.mainloop()
    elif t1 == t2:
        plt.plot(x, y)
        plt.show()

def bt_click2():
    lb5["text"] = ed.get()
    e = ed.get()
    y.append(e)
def bt_click3():
    lb6["text"] = ed2.get()
    q = ed2.get()
    x.append(q)
#----------------------------------------------------------------------------------
#ENTRY
#---------------------------------------------------------------------------------
ed = Entry(janela)
ed.place(x=30,y=50)
ed2 = Entry(janela)
ed2.place(x=30,y=150)
#----------------------------------------------------------------------------------
#BUTTONS
#----------------------------------------------------------------------------------
bt = Button(janela, width=20, text='Gerar Gráfico', font='Times_New_Roman',command=bt_click)
bt.place(x=30 , y=230)
bt2 = Button(janela, width=5, text='Ok', font='Times_New_Roman',command=bt_click2)
bt2.place(x=30,y=80)
bt3 = Button(janela, width=5, text='Ok', font='Times_New_Roman',command=bt_click3)
bt3.place(x=30,y=180)
#-----------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#Labels
lb = Label(janela,text='Rendimento Da Evil Corp', font='Times_New_Roman')
lb.place(x=30, y=20)
lb1 = Label(janela,text='Digite o mês, ano ou dia para gerar o gráfico ', font='Times_New_Roman')
lb1.place(x=30,y=120)
lb3 = Label(janela,text='Valor Digitado de X', font='Times_New_Roman')
lb3.place(x=350,y=150)
lb4 = Label(janela,text='Valor Digitado de Y', font='Times_New_Roman')
lb4.place(x=350,y=220)
lb5 = Label(janela,text='X', font='Times_New_Roman')
lb5.place(x=350,y=180)
lb6 = Label(janela,text='Y', font='Times_New_Roman')
lb6.place(x=350,y=250)
#--------------------------------------------------------------------------------------
janela.geometry('500x300+200+200')
janela.resizable(width=0,height=0)
janela.mainloop()


