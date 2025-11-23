import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

root.configure(bg="black")

def time():
    string = strftime("%H:%M:%S %p\n %d-%m-%Y")
    label.config(text=string)
    label.after(1000, time)  

label = tk.Label(root, font=("black", 50, "bold"), background="white", foreground="black", padx=20, pady=20)
label.pack(anchor="center")

time()  
root.mainloop()
