import tkinter as tk

window = tk.Tk()
Label = tk.Label
window.title("Titel")
lbl = Label(window, text="By JoMei9019", fg='green', font=("Helvetica", 12))
lbl.place(x=66, y=80)
window.geometry("400x250")
#window.resizable(False,False)
#window.iconphoto(False, tk.PhotoImage(file=resource_path("Logo.png")))


window.mainloop()
