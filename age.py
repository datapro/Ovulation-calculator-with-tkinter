from tkinter import *
from tkinter import messagebox as mb 
from datetime import date

# defining your functions
def different_date():
  given_year_field.config(state="normal")
  given_month_field.config(state="normal")
  given_day_field.config(state="normal")
# temproary disable the different_date function
  different_date_button.config(state="disabled")
  # configuring the current day button to normal
  current_date_button.config(state="normal")
# function to set the current to entry field 
def current_date():
  given_year_field.config(state="disabled")
  given_month_field.config(state="disabled")
  given_day_field.config(state="disabled")
  
  #configuring the state of the different date button to normal
  different_date_button.config(state="normal")
  
  #setting the values of the object of StringVar() class to current date in the given date row
  given_year_var.set(current_year)
  given_month_var.set(current_month)
  given_day_var.set(current_day)
def reset_entries():
  birth_year_field.delete(0,END)
  birth_month_field.delete(0,END)
  birth_day_field.delete(0,END)
  # temporarily disable the entries in the given date row
  given_year_field.config(state="disabled")
  given_month_field.config(state="disabled")
  given_day_field.config(state="disabled")
  # configuring the state of the different_date button to normal
  different_date_button.config(state="normal")
    # configuring the current day button to normal
  current_date_button.config(state="normal")
  #setting the values of the object of StringVar() class to current date in the given date row
  given_year_var.set(current_year)
  given_month_var.set(current_month)
  given_day_var.set(current_day)
  # setting the value of object of the StringVar() to empty in the result row
  age_var.set("")
  
  # setting the focus to the birth year field
  birth_year_field.focus_set()
  
def reset():
   # reset entry widget
   reset_entries()
   # show a messagebox that displays success message
   mb.showinfo("Reset Entries", "All has been reset successfully")
def check_for_error():
  # if any field is empty return a messagebox to display error
  if (birth_year_field.get()=="" or birth_month_field.get()=="" or birth_day_field.get()=="" or given_year_field.get()=="" or given_month_field.get()=="" or given_day_field.get()==""):
    mb.showerror("input Error","Invalid Format! Please try again")
    # reset the reset entries
    reset_entries()
    
    # returning -1
    return -1
# to calculate for age
def calculate_age():
  val=check_for_error()
  #checking
  if val == -1:
    return
  else:
    birth_year=int(year_var.get())
    birth_month=int(month_var.get())
    birth_day=int(day_var.get())
    given_year=int(given_year_var.get())
    given_month=int(given_month_var.get())
    given_day=int(given_day_var.get())
    try:
      birth_date=date(birth_year,birth_month,birth_day)
      given_date=date(given_year,given_month,given_day)
      
      # checking if the birth date is less or equal a given date
      if(birth_date < given_date):
        days_left=given_date - birth_date
        # calculate the age in year
        age=int(abs((days_left.total_seconds())/(365 * 24 * 3600)))
        # setting the result as a StringVar() class
        age_var.set(str(age) + "Years old")
      else:
        #display the error if the birth date exceed the given date
        mb.showerror("input Error","Birth date exceed given date.")
        # call your reset entery function to reste the data
        reset_entries()
        
        #raising an exception for value error
    except ValueError:
      mb.showerror("out of range", "Entered date is out of range")
      # calling the reset entrie function to reset the data
      reset_entries()

#main function
if __name__=="__main__":
  root=Tk()
  root.title("Age Calculator-By Emmanuel")
  root.geometry("600x450+650+250")
  root.resizable(0,0)
  root.configure(bg="beige")
  #root.iconbitmap("calendar_img.ico")
  # creating of frame
  header_frame=Frame(root, bg="gray")
  entry_frame=Frame(root, bg="gray")
  result_frame=Frame(root, bg="gray")
  
  # geometry the frame
  header_frame.pack(pady=10)
  entry_frame.pack(pady=10)
  result_frame.pack(pady=10)
  
  # create label to display name of the application
  header_label=Label(header_frame, text="AGE CALCULATOR", bg="gray", fg="beige", font="mssanserif 30")
  header_label.pack(fill="both", pady=10)
  year_label=Label(entry_frame,bg="gray", fg="beige", font="mssanserif 10", text="Year")
  month_label=Label(entry_frame,bg="gray", fg="beige", font="mssanserif 10", text="Month")
  day_label=Label(entry_frame,bg="gray", fg="beige", font="mssanserif 10", text="Day")
  dob_label=Label(entry_frame,bg="gray", fg="beige", font="mssanserif 10", text="Date of Birth")
  given_date_label=Label(entry_frame,bg="gray", fg="beige", font="mssanserif 10", text="Given Date")
  
  # geometry the widget
  year_label.grid(column=1, row=0, padx=10, pady=10)
  month_label.grid(column=2, row=0, padx=10, pady=10)
  day_label.grid(column=3, row=0, padx=10, pady=10)
  dob_label.grid(column=0, row=1, padx=10, pady=10)
  given_date_label.grid(column=0, row=4, padx=10, pady=10)
  
  # sorting the current date
  current_year=date.today().year
  current_month=date.today().month
  current_day=date.today().day
  
  # creating StringVar() class
  year_var=StringVar(entry_frame)
  month_var=StringVar(entry_frame)
  day_var=StringVar(entry_frame)
  
  given_year_var=StringVar(entry_frame)
  given_month_var=StringVar(entry_frame)
  given_day_var=StringVar(entry_frame)
  
  # setting initial value for the object
  year_var.set("")
  month_var.set("")
  day_var.set("")
  
  given_year_var.set(current_year)
  given_month_var.set(current_month)
  given_day_var.set(current_day)
  # widget
  birth_year_field=Entry(entry_frame,width=6, font="mssanserif 10", 
                       textvariable=year_var, justify=CENTER, relief=GROOVE)
  birth_month_field=Entry(entry_frame,width=4, font="mssanserif 10", 
                       textvariable=month_var, justify=CENTER, relief=GROOVE)
  birth_day_field=Entry(entry_frame,width=4, font="mssanserif 10", 
                       textvariable=day_var, justify=CENTER, relief=GROOVE)
  given_year_field=Entry(entry_frame,width=4, font="mssanserif 10", 
                       textvariable=given_year_var, justify=CENTER, relief=GROOVE, state="disabled")
  given_month_field=Entry(entry_frame,width=4, font="mssanserif 10", 
                       textvariable=given_month_var, justify=CENTER, relief=GROOVE, state="disabled")
  given_day_field=Entry(entry_frame,width=4, font="mssanserif 10", 
                       textvariable=given_day_var, justify=CENTER, relief=GROOVE, state="disabled")
  # geometry of entry widget
  birth_year_field.grid(row=1, column=1, padx=10, pady=10)
  birth_month_field.grid(row=1, column=2, padx=10, pady=10)
  birth_day_field.grid(row=1, column=3, padx=10, pady=10)
  
  given_year_field.grid(row=4, column=1, padx=10, pady=10)
  given_month_field.grid(row=4, column=2, padx=10, pady=10)
  given_day_field.grid(row=4, column=3, padx=10, pady=10)
  # creating the button to manipulate the entry field
  different_date_button=Button(entry_frame,text="Different_date", 
                               command=different_date, font="mssanserif 10", width=14,bg="beige", fg="gray", disabledforeground="#907957")
  current_date_button=Button(entry_frame,text="Current_date", 
                               command=current_date, font="mssanserif 10", width=14,bg="beige", fg="gray", disabledforeground="#907957")
  # geometer the button widget
  different_date_button.grid(row=4,column=4, padx=10, pady=10)
  current_date_button.grid(row=7,column=4, padx=10, pady=10)
  #  creating an object of intVar() class
  age_var=StringVar(result_frame)
  age_var.set("")
  
  # foot widget
  footer_label=Label(result_frame,text="The calculated age is", bg="beige", fg="gray", font=("mssanserif", "10","bold"))
  age_label=Label(result_frame, textvariable=age_var, bg="beige", fg="gray", font=("mssanserif", "10","bold"), width=10)
  # geometry
  footer_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
  age_label.grid(row=0, column=1, padx=10, pady=10, sticky=W)
  reset_button=Button(result_frame, text="Reset Button", width=12, font="mssanserif 10", command=reset, bg="beige", fg="gray")
  calculate_button=Button(result_frame, text="Calculate Button", width=12, font="mssanserif 10", command=calculate_age, bg="beige", fg="gray")
  # geometry the widget
  reset_button.grid(row=1,column=0, padx=10, pady=10)
  calculate_button.grid(row=1,column=1, padx=10, pady=10)
  root.mainloop()
  
      
  
    
  
  
  

  