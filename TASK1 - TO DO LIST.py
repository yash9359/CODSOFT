from tkinter import *
from tkinter import messagebox
class todoapp:
    
    def __init__(self):
        self.td=Tk()
        self.td.title("TO Do List App")
        self.td.geometry('600x500')
        

        self.n1=Label(self.td,text='TO DO LIST',font=("Helvitica",16,"bold"), bg="#A7C037")
        self.n1.pack(pady=15)

        self.e1=Entry(self.td,bg='white', font=("Helvetica", 10),width=30)
        self.e1.pack(padx=15,pady=10)


        self.b1=Button(self.td,text="ADD TASK ",bg="#28a745", fg="white",command=self.add_task)
        self.b1.pack(pady=10)


        self.l1=Listbox(self.td,font=("Helvitica",10),width=40,height=10)
        self.l1.pack(padx=5,pady=10,)
        
        self.b1=Button(self.td, text="Mark as Done", command=self.mark_done, bg="#17b86a", fg="white")
        self.b1.pack(pady=5)
        
        self.b2=Button(self.td, text="Delete Task", command=self.delete_task, bg="#dc35aa", fg="white")
        self.b2.pack(pady=5)

        entry_frame = Frame(self.td)
        entry_frame.pack(pady=10)

        self.e2= Entry(entry_frame, bg='white', font=("Helvetica", 10), width=30)
        self.e2.pack(side=LEFT, padx=(0, 5))

        self.b3 = Button(entry_frame, text='UPDATE', command=self.update_task, bg="#c1c346", fg="white")
        self.b3.pack(side=LEFT,pady = 2)
        
        self.td.configure(bg="#346C9D")
        self.td.mainloop()


    def add_task(self):
        input_text = self.e1.get().strip()
        if input_text == "":
            messagebox.showwarning("Warning", "Please enter a task.")
            return
        task = "❌" + input_text
        self.l1.insert(END, task)
        self.e1.delete(0, END)


    def mark_done(self):
        selected = self.l1.curselection()
        
        if not selected:
            messagebox.showinfo("Info", "Select a task to mark as done.")
            return
        index = selected[0]
        task = self.l1.get(index)
        if not task.startswith("✅"):
            task = task.replace("❌", "✅", 1)
            self.l1.delete(index)
            self.l1.insert(index, task)


        
    def delete_task(self):
        sel=self.l1.curselection()
        if not sel:
            messagebox.showinfo("Info","Select a task to be deleted.")
            return
        self.l1.delete(sel)

    def update_task(self):
        selected = self.l1.curselection()
        new_text = self.e2.get().strip()

        if not selected:
            messagebox.showinfo("Info", "Select a task to update.")
            return

        if new_text == "":
            messagebox.showwarning("Warning", "Please enter the updated task.")
            return

        index = selected[0]
        old_task = self.l1.get(index)

        status = old_task[0] if old_task[0] in ['❌', '✅'] else ''
        updated_task = status + new_text

        self.l1.delete(index)
        self.l1.insert(index, updated_task)
        self.e2.delete(0, END)


start=todoapp()


