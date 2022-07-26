from tkinter import *
from tkinter import Tk,ttk
from PIL import Image,ImageTk
from tkinter import filedialog as fd
import cv2


co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit

janela=Tk()
janela.title("")
janela.geometry("300x356")
janela.configure(background=co1)
janela.resizable(width=False,height=False)


#abrindo img para logo
imagem=Image.open('icon.png')
imagem=imagem.resize((50,50))
imagem=ImageTk.PhotoImage(imagem)

app_logo=Label(janela,text='Imagem para > Desenho a lápis',image=imagem,width=300,compound=LEFT,relief=RAISED,anchor=NW,font=('System 9 bold'),bg=co1,fg=co4)
app_logo.place(x=0,y=0)


#funcao para escolher imagem
global imagem_original,l_img,img_manipulada

imagem_original=['']

def escolher_imagem():
    global imagem_original,l_img,img_manipulada

    imagem_escolher=fd.askopenfilename()
    imagem_original.append(imagem_escolher)
    
    


    #abrindon a img
    img_manipulada=Image.open(imagem_escolher)
    img_manipulada=img_manipulada.resize((170,170))
    img_manipulada=ImageTk.PhotoImage(img_manipulada)

    l_img=Label(janela,image=img_manipulada,bg=co1,fg=co4)
    l_img.place(x=60,y=60)


#funcao converter img

def converter_imagem():
    global imagem_original,l_img,img_manipulada
    
    
    valor_escala=escala.get()
    
    imagem= cv2.imread(imagem_original[-1] ) 
    
    #converter uma imagem de um espaço de cores para outra cor
    imagem_cinza=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
    
    desfoco=cv2.GaussianBlur(imagem_cinza,(21,21),0,0)
    
    lapis=cv2.divide(imagem_cinza,desfoco,scale=valor_escala)
    
    cv2.imwrite('img/imagem_convertida.png',lapis)
    
    
    #abrindo img que foi convertida
    img_manipulada=Image.open('img/imagem_convertida.png')
    img_manipulada=img_manipulada.resize((170,170))
    img_manipulada=ImageTk.PhotoImage(img_manipulada)

    l_img=Label(janela,image=img_manipulada,bg=co1,fg=co4)
    l_img.place(x=60,y=60)


#------opcpes--------

l_opcoes=Label(janela,text='Configurações-------------------------------------------'.upper(),anchor=NW,font=('Verdana 7 bold'),bg=co1,fg=co4)
l_opcoes.place(x=10,y=260)


escala=Scale(janela,command=converter_imagem,from_=0,to=255,length=120,bg=co1,fg='red',orient=HORIZONTAL)
escala.place(x=10,y=300)

b_escolher=Button(janela,command=escolher_imagem,text='Escolher imagem',width=15,overrelief=RIDGE,font=('Ivy 10'),bg=co1,fg=co4)
b_escolher.place(x=147,y=287)

b_salvar=Button(janela,command=converter_imagem,text='Salvar',width=15,overrelief=RIDGE,font=('Ivy 10'),bg=co2,fg=co1)
b_salvar.place(x=147,y=317)


janela.mainloop()
