import tkinter
import tkinter.messagebox
import random

root = tkinter.Tk()
root.title("Perpustakaan Makmur")
root.geometry("300x300")

class Queue_Habit(object):
    def __init__(self):
        self.task = []

    def clear_listbox(self):
        lb_tasks.delete(0, "end")

    def update_listbox(self):
        self.clear_listbox()
        for ts in self.task:
                lb_tasks.insert("end", ts)
                
    def len_task(self):
        count = len(self.task)
        message = "Jumlah Buku: %s" %count
        lbl_display["text"] = message

    def search(self):
        tasks = txt_input.get()
        if tasks == "":
            tkinter.messagebox.showwarning("Warning", "Ketik dulu!")
       
        else :
             if tasks in self.task:
                message = "buku %s tersedia" %tasks
                lbl_display["text"] = message
             else :
                message = "buku %s tidak tersedia" %tasks
                lbl_display["text"] = message
        txt_input.delete(0, "end")
        
    def enqueue(self):
        tasks = txt_input.get()
        if tasks != "":
                self.task.append(tasks)
                self.task.sort()
                self.update_listbox()
        else:
                tkinter.messagebox.showwarning("Warning", "Masukan Data")
        txt_input.delete(0, "end")

    def dequeue(self):
        confirmed = tkinter.messagebox.askyesno("Please Confirm", " Urutkan Dari Bawah")
        if confirmed == True :
            self.task.reverse()
            self.update_listbox()
        
    def remove_all(self):
        confirmed = tkinter.messagebox.askyesno("Please Confirm", " hapus semua ?")
        if confirmed == True :
            self.task = []
            self.update_listbox()

    def remove_one(self):
        tasks = lb_tasks.get("active")
        confirmed = tkinter.messagebox.askyesno("Please Confirm", "hapus ?")
        if confirmed == True :
            self.task.remove(tasks)
            self.update_listbox()
        
        
QH = Queue_Habit()

lbl_display = tkinter.Label(root, text="")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=20)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="Tambah", bg="grey", command = QH.enqueue)
btn_add_task.grid(row=1,column=0)

btn_del_one = tkinter.Button(root, text="Urutan", bg="blue", command= QH.dequeue)
btn_del_one.grid(row=2,column=0)

btn_remove_one = tkinter.Button(root, text="Hapus", bg="orange", command= QH.remove_one)
btn_remove_one.grid(row=3,column=0)

btn_remove_all = tkinter.Button(root, text="Hapus Semua", bg="pink", command= QH.remove_all)
btn_remove_all.grid(row=4,column=0)

btn_number_of_tasks = tkinter.Button(root, text="Jumlah Buku", bg="green", command = QH.len_task)
btn_number_of_tasks.grid(row=1,column=2)

btn_search = tkinter.Button(root, text="Cari", bg="yellow", command = QH.search)
btn_search.grid(row=2,column=2)

btn_exit = tkinter.Button(root, text="Keluar", bg="red", command=exit)
btn_exit.grid(row=3,column=2)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1, rowspan=7)

root.mainloop()
