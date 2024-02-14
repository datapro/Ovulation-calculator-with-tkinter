import tkinter as tk 
def ci():
  p=float(entry1.get())
  n=float(entry2.get())
  r=float(entry3.get())
  t=float(entry4.get())
  i= p * ((1 + (r/100))**t)
  c.set(i-p) 
# def compound():
#   p=entry1.get()

root=tk.Tk()
root.title("compund interest calcultor")
root.geometry("500x500")
entry1=tk.Entry(root)
entry2=tk.Entry(root)
entry3=tk.Entry(root)
entry4=tk.Entry(root)
lbl2=tk.Label(root, text="Principal")
c=tk.StringVar()
# A=tk.StringVar()
lbl=tk.Label(root, textvariable=A)
lbl1=tk.Label(root, textvariable=c)
calcBtn=tk.Button(root,command=ci, text="Compound")
# calcBtn1=tk.Button(root,command=compound, text="Compound interest")
lbl2.grid(row=0, column=0)  
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=0)
entry3.grid(row=3, column=0)
entry4.grid(row=4, column=0)
calcBtn.grid(row=5, column=0, columnspan=2)
# calcBtn1.grid(row=6, column=0, columnspan=2)
lbl.grid(row=6, column=0, columnspan=2)
lbl1.grid(row=7, column=0, columnspan=2)

root.mainloop()
  

  
  
  
  