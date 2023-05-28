import tkinter as tk

window = tk.Tk()
Label = tk.Label
window.title("Titel")
lbl = Label(window, text="By JoMei9019", fg='green', font=("Helvetica", 12))
lbl.place(x=66, y=80)
window.geometry("400x250")
window.resizable(False,False)       #Delete line, if window should be resizable!


window.mainloop()
