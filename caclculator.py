import tkinter as tk 

def add():
  num1=float(entry1.get())
  num2=float(entry2.get())
  result.set(num1 + num2)
  
# window
root=tk.Tk()
root.title("A basic calculator")
root.geometry("100x100+650+250")
# widget
entry1=tk.Entry(root)
entry2=tk.Entry(root)

# create a stringvar to store your result
result=tk.StringVar()
lbl=tk.Label(root, textvariable=result)
addBtn=tk.Button(root, command=add, text="Addiction")
# Geometry
entry1.grid(row=0, column=0)
entry2.grid(row=1, column=0)
addBtn.grid(row=2, column=0, columnspan=2)
lbl.grid(row=3,column=0, columnspan=2)

root.mainloop()