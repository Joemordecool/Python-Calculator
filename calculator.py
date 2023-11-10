import tkinter as tk
import os
import sys

# Button actions
def click_event(key, event=None):

	# = -> Calculate results
    if key == '=' or (event and event.keysym == 'Return'):
        # Safeguard against integer division
        if '/' in entry.get() and '.' not in entry.get():
            entry.insert(tk.END, ".0")
			
        # Attempt to evaluate results
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Operation")
	
    elif key=="x":
        entry.insert(tk.END, "*")
 		
	# C -> Clear entry		
    elif key == 'C':
        entry.delete(0, tk.END)
	
    # ⌫ -> Clear last char
    elif key=='⌫':
        entry.delete(len(entry.get())-1,tk.END)
 	
	# Clear entry and start new input		
    else:
        if '=' in entry.get():
            entry.delete(0, tk.END)
        entry.insert(tk.END, key)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
        
    return os.path.join(base_path, relative_path)

# GUI Start

window=tk.Tk()
window.geometry("350x500")
window.title("Calculator")
path=resource_path('calculatorIcon.png')
logo=tk.PhotoImage(file=path)
window.iconphoto(True, logo)
window.bind('<Return>', lambda event: click_event('=', event))

# Responsive buttons

for i in range(6):                                  
    window.grid_rowconfigure(i, weight=1)
for i in range(4):                                  
    window.grid_columnconfigure(i, weight=1)

# Buttons

buttons = [
'7',  '8',  '9',  'x',  
'4',  '5',  '6',  '/', 
'1',  '2',  '3',  '-',  
'0',  '.',  '=',  '+',  
'C', '⌫']

# GUI Setup

row = 1
col = 0
for i in buttons:
    action = lambda x = i: click_event(x)
    if row < 5:
        tk.Button(window, text = i, width = 2, height = 2, command = action,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050") \
		    .grid(row = row, column = col, sticky = 'nesw', )
    elif row==5:
        tk.Button(window, text = i, width = 2, height = 2, command = action,font=("Lucida Console",20,"bold"), fg="#CCCCCC", bg="#505050") \
            .grid(row = row, column = col, columnspan = 2, sticky = 'nesw', )
        col+=1
    col += 1
    if col > 3:
        col = 0
        row += 1
        
# Entrybox

entry=tk.Entry(window,width=40, bg="#505050",bd=10,font=("Lucida Console",20,"bold"),fg="#CCCCCC")
entry.grid(row=0,column=0,columnspan=4,sticky="nsew")

# Program Start

window.mainloop()