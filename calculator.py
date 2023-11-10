from tkinter import *

# Acciones de los botones

def button_1_click():
    entry.insert(END, "1")
    
def button_2_click():
    entry.insert(END, "2")
    
def button_3_click():
    entry.insert(END, "3")

def button_4_click():
    entry.insert(END, "4")

def button_5_click():
    entry.insert(END, "5")

def button_6_click():
    entry.insert(END, "6")
    
def button_7_click():
    entry.insert(END, "7")
    
def button_8_click():
    entry.insert(END, "8")

def button_9_click():
    entry.insert(END, "9")

def button_0_click():
    entry.insert(END, "0")

def button_plus_click():
    entry.insert(END, "+")

def button_minus_click():
    entry.insert(END, "-")

def button_multiply_click():
    entry.insert(END, "*")

def button_divide_click():
    entry.insert(END, "/")

def button_clear_click():
    entry.delete(0, END)

def button_comma_click():
    entry.insert(END, ".")

def button_equal_click(event=None):
    result=0
    expression = entry.get()
    try:
        result = eval(expression)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error, use only valid chars")
        window.after(5000, lambda: entry.delete(0, END))
    else:
        if type(result)==float and result%1==0:
            result=int(result)
        entry.delete(0, END)
        entry.insert(END, result)

def insert_char(event):
    if event.char.isdigit() or event.char in "+-*/.":
        entry.insert(END, event.char) 

def button_backspace_click(event=None):
    entry.delete(len(entry.get())-1,END)


# Inicializacion de la ventana (tamaño, icono, titulo)

window=Tk()
window.geometry("350x500")
window.title("Calculator")
logo=PhotoImage(file='C:/Users/josei/OneDrive/Escritorio/Code/Python/Calculator/calculatorIcon.png')
window.iconphoto(True, logo)
window.bind("<Key>", insert_char)
window.bind("<BackSpace>", lambda event: button_backspace_click(event))
window.bind("<Return>", lambda event: button_equal_click(event))

# Responsive buttons

# El rango es segun la cantidad X de filas o columnas que tenga

for i in range(8):                                  # Filas
    window.grid_rowconfigure(i, weight=1)
for i in range(4):                                  # Columnas
    window.grid_columnconfigure(i, weight=1)


# Buttons

# Botones con los parametros y agrego el grid para distribuirlos

# El sticky hace que sea responsivo si agrando o no la ventana

# NOTA: El grid agregarlo siempre despues de poner el boton, no junto al crearlo, porque al hacer eso, creo el boton y al agregar el grid despues
# se asigna en type "None", y la hacer los calculos falla la asignacion

button_1=Button(window, text="1", width=2, height=2,command=button_1_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_1.grid(row=5,column=0,sticky="nsew")       

button_2=Button(window, text="2", width=2, height=2,command=button_2_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_2.grid(row=5,column=1,sticky="nsew")

button_3=Button(window, text="3", width=2, height=2,command=button_3_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_3.grid(row=5,column=2,sticky="nsew")

button_4=Button(window, text="4", width=2, height=2,command=button_4_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_4.grid(row=4,column=0,sticky="nsew")

button_5=Button(window, text="5", width=2, height=2,command=button_5_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_5.grid(row=4,column=1,sticky="nsew")

button_6=Button(window, text="6", width=2, height=2,command=button_6_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_6.grid(row=4,column=2,sticky="nsew")

button_7=Button(window, text="7", width=2, height=2,command=button_7_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_7.grid(row=3,column=0,sticky="nsew")

button_8=Button(window, text="8", width=2, height=2,command=button_8_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_8.grid(row=3,column=1,sticky="nsew")

button_9=Button(window, text="9", width=2, height=2,command=button_9_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_9.grid(row=3,column=2,sticky="nsew")

button_0=Button(window, text="0", width=2, height=2,command=button_0_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_0.grid(row=6,column=0,sticky="nsew")

button_comma=Button(window, text=",", width=2, height=2,command=button_comma_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_comma.grid(row=6,column=1,sticky="nsew")

button_equal=Button(window, text="=", width=2, height=2,command=button_equal_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_equal.grid(row=6,column=2,sticky="nsew")

button_plus=Button(window, text="+", width=2, height=2,command=button_plus_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_plus.grid(row=6,column=3,sticky="nsew")

button_minus=Button(window, text="-", width=2, height=2,command=button_minus_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_minus.grid(row=5,column=3,sticky="nsew")

button_multiply=Button(window, text="x", width=2, height=2,command=button_multiply_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_multiply.grid(row=4,column=3,sticky="nsew")

button_divide=Button(window, text="/", width=2, height=2,command=button_divide_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_divide.grid(row=3,column=3,sticky="nsew")

button_clear=Button(window, text="C", width=2, height=2,command=button_clear_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_clear.grid(row=7,column=0,columnspan=2,sticky="nsew")

button_backspace=Button(window, text="⌫", width=2, height=2,command=button_backspace_click,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050")
button_backspace.grid(row=7,column=2,columnspan=2,sticky="nsew")

# Entrybox

entry=Entry(window, bg="#505050",bd=10,font=("Lucida Console",20,"bold"),fg="#CCCCCC")
entry.grid(row=0,column=0,columnspan=4,rowspan=3,sticky="nsew")


# Inicio de programa

window.mainloop()