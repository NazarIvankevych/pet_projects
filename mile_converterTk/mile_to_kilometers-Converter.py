<<<<<<< HEAD
from tkinter import *

# Make a logic for all components
def get_info():
    miles_into_km = float(user_insert.get())
    result = miles_into_km * 1.609344
    converter_result.config(text=int(result), bg='blue', fg='yellow')

display = Tk()
display.title("Mile to Km Converter")
display.minsize(height=400, width=400)
# Text from user
user_insert = Entry(width=10, font=("Arial", 20))
user_insert.grid(column=2, row=1)
user_format = Label(text="Miles")
user_format.grid(column=3, row=1)
# Text from converter
converter_text = Label(text="Is equal to", font=("Arial", 20))
converter_result = Label(text="0", font=("Arial", 20))
converter_format = Label(text="Km", font=("Arial", 20))

converter_text.grid(column=1, row=2, pady=2)
converter_result.grid(column=2, row=2, pady=2)
converter_format.grid(column=3, row=2, pady=2)
# Button to activate converting
user_check = Button(text="Calculate", font=("Arial", 20), command=get_info)
user_check.grid(column=2, row=3, pady=2)

=======
from tkinter import *

# Make a logic for all components
def get_info():
    miles_into_km = float(user_insert.get())
    result = miles_into_km * 1.609344
    converter_result.config(text=int(result), bg='blue', fg='yellow')

display = Tk()
display.title("Mile to Km Converter")
display.minsize(height=400, width=400)
# Text from user
user_insert = Entry(width=10, font=("Arial", 20))
user_insert.grid(column=2, row=1)
user_format = Label(text="Miles")
user_format.grid(column=3, row=1)
# Text from converter
converter_text = Label(text="Is equal to", font=("Arial", 20))
converter_result = Label(text="0", font=("Arial", 20))
converter_format = Label(text="Km", font=("Arial", 20))

converter_text.grid(column=1, row=2, pady=2)
converter_result.grid(column=2, row=2, pady=2)
converter_format.grid(column=3, row=2, pady=2)
# Button to activate converting
user_check = Button(text="Calculate", font=("Arial", 20), command=get_info)
user_check.grid(column=2, row=3, pady=2)

>>>>>>> 6bb0f90e7b2042da98278b61b14da243c44df510
display.mainloop()