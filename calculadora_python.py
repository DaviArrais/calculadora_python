from tkinter import *
janela=Tk()
janela.title("Calculadora Tkinter - Matemática - IMC")
janela.geometry("1000x500")
#Funções
def percentual():
    pass
#Janela Matematica
LabelFrame_calculadora=LabelFrame(janela,text="MATEMÁTICA",borderwidth=1, relief="solid")
LabelFrame_calculadora.place(x=20,y=20, width=470, height=460)
Frame_calculadora=Frame(LabelFrame_calculadora,borderwidth=1, relief="solid")
Frame_calculadora.place(x=20,y=20, width=430, height=100)
botao_percentual=Button(LabelFrame_calculadora, text="%",command=percentual)
botao_percentual.place(x=25,y=140, width=90, height=44) 
botao_limpar=Button(LabelFrame_calculadora, text="C",command=percentual)
botao_limpar.place(x=135,y=140, width=90, height=44) 
botao_quadrado=Button(LabelFrame_calculadora, text="X2",command=percentual)
botao_quadrado.place(x=245,y=140, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="/",command=percentual)
botao_percentual.place(x=355,y=140, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="X",command=percentual)
botao_percentual.place(x=355,y=199, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="-",command=percentual)
botao_percentual.place(x=355,y=258, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="+",command=percentual)
botao_percentual.place(x=355,y=317, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="=",command=percentual)
botao_percentual.place(x=355,y=372, width=90, height=44) 
Frame_numero=Frame(LabelFrame_calculadora,borderwidth=1)
Frame_numero.place(x=20,y=204, width=315, height=215)
botao_7=Button(Frame_numero, text="7",command=percentual)
botao_7.place(x=3,y=0, width=90, height=38) 
botao_8=Button(Frame_numero, text="8",command=percentual)
botao_8.place(x=113,y=0, width=90, height=38) 
botao_9=Button(Frame_numero, text="9",command=percentual)
botao_9.place(x=223,y=0, width=90, height=38) 
botao_4=Button(Frame_numero, text="4",command=percentual)
botao_4.place(x=3,y=58, width=90, height=38) 
botao_5=Button(Frame_numero, text="5",command=percentual)
botao_5.place(x=113,y=58, width=90, height=38) 
botao_6=Button(Frame_numero, text="6",command=percentual)
botao_6.place(x=223,y=58, width=90, height=38) 
botao_1=Button(Frame_numero, text="1",command=percentual)
botao_1.place(x=3,y=116, width=90, height=38) 
botao_2=Button(Frame_numero, text="2",command=percentual)
botao_2.place(x=113,y=116, width=90, height=38) 
botao_3=Button(Frame_numero, text="3",command=percentual)
botao_3.place(x=223,y=116, width=90, height=38) 
botao_0=Button(Frame_numero, text="0",command=percentual)
botao_0.place(x=3,y=174, width=90, height=38) 
botao_v=Button(Frame_numero, text=",",command=percentual)
botao_v.place(x=113,y=174, width=90, height=38) 
botao_a=Button(Frame_numero, text="<",command=percentual)
botao_a.place(x=223,y=174, width=90, height=38) 



#Janela IMC
def calcular_imc():
    pass

LabelFrame_imc=LabelFrame(janela,text="IMC",borderwidth=1, relief="solid")
LabelFrame_imc.place(x=510,y=20, width=470, height=460)
Frame_imc=Frame(LabelFrame_imc,borderwidth=1, relief="solid").place(x=20,y=20, width=430, height=100)

Label(LabelFrame_imc,text="Peso", font= "20", anchor=W).place(x=80, y=150, width=50, height=50)
peso=Entry(LabelFrame_imc).place(x=140, y=153, width=100, height=50)
Label(LabelFrame_imc,text="Altura", font= "20", anchor=W).place(x=80, y=230, width=50, height=80)
altura=Entry(LabelFrame_imc).place(x=140, y=243, width=100, height=50)
Button(LabelFrame_imc,text="Calcular IMC", command=calcular_imc).place(x=140, y=330, width=100, height=50)

Frame_imc_indice=Frame(LabelFrame_imc, borderwidth=1, relief="solid" ).place(x=290,y=313, width=120, height=80)

janela.mainloop()