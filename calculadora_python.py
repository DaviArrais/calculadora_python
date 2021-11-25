
#Importe de bibliotecas
from tkinter import *
from tkinter import ttk
from typing import ValuesView
#Declaração da janela
janela=Tk()
janela.title("Calculadora Tkinter - Matemática - IMC")
janela.geometry("510x500")
#Declaração das abas
aba=ttk.Notebook(janela)
aba.place(x=20,y=20, width=470, height=460)
#Variavel para receber comandos
lista_comandos=[]
var=StringVar()
n1=StringVar()
numerador=0
op=""
#Funções associadas aos botões

def num1():
    lista_comandos.append(1)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador= var.get() 
def num2():
    lista_comandos.append(2)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador=int(operador)
    numerador= var.get() 
def num3():
    lista_comandos.append(3)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador= var.get() 
def num4():
    lista_comandos.append(4)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador= var.get() 
def num5():
    lista_comandos.append(5)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador= var.get() 
def num6():
    lista_comandos.append(6)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador= var.get() 
def num7():
    lista_comandos.append(7)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador= var.get() 
def num8():
    lista_comandos.append(8)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador= var.get() 
def num9():
    lista_comandos.append(9)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador= var.get()    
def num0():
    lista_comandos.append(0)
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
    numerador=int(operador)
def igual():
    retorno=0
    x1=float(n1.get())
    x2=float(var.get())
    if op=="+":
        retorno=x1+x2
    elif op=="-":
       retorno=x1-x2 
    elif op=="*":
       retorno=x1*x2 
    elif op=="/":
       retorno=x1/x2 
    elif op=="%":
       retorno=(x1/100)*x2   
    elif op=="x2":
       retorno=x1**x2  
    elif op=="%":
       retorno=(x1/100)*x2  
    var.set(retorno)
def apagar_ultimo(): 
    lista_comandos.pop()
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
def limpar():
    var.set("")
    n1.set("")
    for x in range(0,len(lista_comandos)):
        lista_comandos.pop() 
def percentual(): 
    n=var.get()
    n1.set(n)
    var.set("%")
    global op
    op="%" 
    for x in range(0,len(lista_comandos)):
        lista_comandos.pop()
def quadrado():
    n=var.get()
    n1.set(n)
    global op
    op="x2" 
    var.set("X2")
    for x in range(0,len(lista_comandos)):
        lista_comandos.pop()
def divisao():
    n=var.get()
    n1.set(n)
    global op
    op="/" 
    var.set("/")
    for x in range(0,len(lista_comandos)):
        lista_comandos.pop()
def multiplicacao():
    n=var.get()
    n1.set(n)
    global op
    op="*" 
    var.set("*")
    for x in range(0,len(lista_comandos)):
        lista_comandos.pop()
def subtracao():
    n=var.get()
    n1.set(n)
    global op
    op="-" 
    var.set("-")
    for x in range(0,len(lista_comandos)):
        lista_comandos.pop()
def soma():
    n=var.get()
    n1.set(n)
    var.set("+")
    global op
    op="+" 
    for x in range(0,len(lista_comandos)):
        lista_comandos.pop()
def virgula():  
    var.set(",")
    lista_comandos.append(".")
    operador=""
    for n in range(0, len(lista_comandos)):
        operador=operador+str(lista_comandos[n])
    var.set(operador)
#Aba calculadora matemática com os elementos
LabelFrame_calculadora=LabelFrame(aba)
aba.add(LabelFrame_calculadora, text="MATEMÁTICA")
Frame_calculadora=Frame(LabelFrame_calculadora,borderwidth=1, relief="solid")
Frame_calculadora.place(x=20,y=20, width=430, height=100)
l=Label(Frame_calculadora, textvariable=n1).pack()
t=Entry(Frame_calculadora, textvariable=var, justify=RIGHT,font=("Arial",25)).place(x=20,y=20, width=390, height=60)
botao_percentual=Button(LabelFrame_calculadora, text="%", background="#9b9695", font=("Arial",25),command=percentual)
botao_percentual.place(x=25,y=140, width=90, height=44) 
botao_limpar=Button(LabelFrame_calculadora, text="C", background="#9b9695", font=("Arial",25),command=limpar)
botao_limpar.place(x=135,y=140, width=90, height=44) 
botao_quadrado=Button(LabelFrame_calculadora, text="X2", background="#9b9695", font=("Arial",25),command=quadrado)
botao_quadrado.place(x=245,y=140, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="/", background="#9b9695", font=("Arial",25),command=divisao)
botao_percentual.place(x=355,y=140, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="X", background="#9b9695", font=("Arial",25),command=multiplicacao)
botao_percentual.place(x=355,y=199, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="-", background="#9b9695", font=("Arial",25),command=subtracao)
botao_percentual.place(x=355,y=258, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="+", background="#9b9695", font=("Arial",25),command=soma)
botao_percentual.place(x=355,y=317, width=90, height=44) 
botao_percentual=Button(LabelFrame_calculadora, text="=", background="#9b9695", font=("Arial",25),command=igual)
botao_percentual.place(x=355,y=372, width=90, height=44) 
Frame_numero=Frame(LabelFrame_calculadora,borderwidth=1)
Frame_numero.place(x=20,y=204, width=315, height=215)
botao_7=Button(Frame_numero, text="7", background="#9383f1", font=("Arial",25),command=num7)
botao_7.place(x=3,y=0, width=90, height=38) 
botao_8=Button(Frame_numero, text="8", background="#9383f1", font=("Arial",25),command=num8)
botao_8.place(x=113,y=0, width=90, height=38) 
botao_9=Button(Frame_numero, text="9", background="#9383f1", font=("Arial",25),command=num9)
botao_9.place(x=223,y=0, width=90, height=38) 
botao_4=Button(Frame_numero, text="4", background="#9383f1", font=("Arial",25),command=num4)
botao_4.place(x=3,y=58, width=90, height=38) 
botao_5=Button(Frame_numero, text="5", background="#9383f1", font=("Arial",25),command=num5)
botao_5.place(x=113,y=58, width=90, height=38) 
botao_6=Button(Frame_numero, text="6", background="#9383f1", font=("Arial",25),command=num6)
botao_6.place(x=223,y=58, width=90, height=38) 
botao_1=Button(Frame_numero, text="1", background="#9383f1", font=("Arial",25),command=num1)
botao_1.place(x=3,y=116, width=90, height=38) 
botao_2=Button(Frame_numero, text="2", background="#9383f1", font=("Arial",25),command=num2)
botao_2.place(x=113,y=116, width=90, height=38) 
botao_3=Button(Frame_numero, text="3", background="#9383f1", font=("Arial",25),command=num3)
botao_3.place(x=223,y=116, width=90, height=38) 
botao_0=Button(Frame_numero, text="0", background="#9383f1", font=("Arial",25),command=num0)
botao_0.place(x=3,y=174, width=90, height=38) 
botao_v=Button(Frame_numero, text=",", background="#9383f1", font=("Arial",25),command=virgula)
botao_v.place(x=113,y=174, width=90, height=38) 
botao_a=Button(Frame_numero, text="<", background="#9383f1", font=("Arial",25),command=apagar_ultimo)
botao_a.place(x=223,y=174, width=90, height=38) 
#Aba IMC
#variáveis utilizados
t1="Informe o peso e a altura!!!"
p = StringVar()
a = StringVar()
imc = StringVar()
indice=0
texto= StringVar()
texto.set(t1)
#Função associada ao botão
def calcular_imc():
    peso=int(p.get())
    altura=float(a.get())
    indice=peso / (altura**2)
    if indice<=18.5:
        t1='Você está abaixo do peso!'
    elif (indice>18.5) and (indice<=25):
        t1='Você está no peso ideal!'
    elif (indice>25) and (indice<=30):
        t1='Você está com sobrepeso!'
    elif (indice>30) and (indice<=40):
        t1='Você está obeso!'
    else:
        t1='Você está com obesidade grave!'
    imc.set(round(indice,2))  
    texto.set(t1)
#Aba calculadora IMC com os elementos
LabelFrame_imc=LabelFrame(aba)
aba.add(LabelFrame_imc, text="IMC")
Frame_imc=Frame(LabelFrame_imc,borderwidth=1, relief="solid").place(x=20,y=20, width=430, height=100)
Label(LabelFrame_imc,text="Peso", font= "20", anchor=W).place(x=80, y=150, width=50, height=50)
peso=Entry(LabelFrame_imc, textvariable=p, font=("Arial",25)).place(x=140, y=153, width=100, height=50)
Label(LabelFrame_imc,text="Altura", font= "20", anchor=W).place(x=80, y=230, width=50, height=80)
altura=Entry(LabelFrame_imc, textvariable=a,font=("Arial",25)).place(x=140, y=243, width=100, height=50)
Button(LabelFrame_imc,text="Calcular IMC", command=calcular_imc, background="#9b9695", font=("Arial",12)).place(x=140, y=330, width=100, height=50)
Label(LabelFrame_imc, textvariable=texto,font=("Arial",20)).place(x=40, y=40, width=380, height=60)
Frame_imc_indice=LabelFrame(LabelFrame_imc, borderwidth=1, relief="solid" ).place(x=290,y=313, width=120, height=80)
Label(LabelFrame_imc, textvariable=imc,font=("Arial",25)).place(x=300, y=330, width=100, height=50)
#Comando para atualização de janela
janela.mainloop()