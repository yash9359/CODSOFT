import tkinter as tk


def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR")

root = tk.Tk()
root.title("CALCULATOR")
root.configure(bg="#857892")

entry = tk.Entry(root, width=20, font=('Arial', 14), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    btn_bg = "#23C466"
    btn_fg = "#000000"
    
    
    if text in ['/', '*', '-', '+']:
        btn_bg = "#E0B60E"
        btn_fg = "#000000"
    elif text == '=':
        btn_bg = "#E0B60E"
        btn_fg = "#000000"
    
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 12, 'bold'),bg=btn_bg, fg=btn_fg,
                       command=lambda t=text: press(t) if t != '=' else calculate())
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="CLEAR", width=9, height=2, font=('Arial', 12), command=clear,bg="black",fg='red')
clear_button.grid(row=5, column=0, columnspan=4)

root.mainloop()
