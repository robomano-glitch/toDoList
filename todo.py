from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To do list')
        self.root.geometry('650x650+300+150')

        self.label2 = Label(self.root, text="Add new task",
            font='ariel, 12 bold', width=9, bd=5, fg='black')
        self.label2.place(x=2, y=10)

        self.label3 = Label(self.root, text="current tasks",
            font='ariel, 12 bold', width=9, bd=5, fg='black')
        self.label3.place(x=2, y=70)

        self.main_text = Listbox(self.root, height=9, font='ariel, 10', width=94, bd=0)
        self.main_text.place(x=2, y=100)

        self.text = Text(self.root, bd=0, height=2, width=30, font='ariel, 10')
        self.text.place(x=2, y=40)

        #====================================add task =======================#
        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()

def main():
    root = ThemedTk(theme="arc")
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()