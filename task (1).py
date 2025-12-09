#محمد عطوه
import tkinter as tk

root = tk.Tk()
lbl = tk.Label(root, text="اختر كلمة")
lbl.pack()

var = tk.StringVar(value="مصر")
tk.OptionMenu(root, var, "مصر", "مصر العالي ", "برمجة", "Python").pack()

tk.Button(root, text="عرض", command=lambda: lbl.config(text=var.get())).pack()

root.mainloop()