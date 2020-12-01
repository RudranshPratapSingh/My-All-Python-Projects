from tkinter import *

root = Tk()

def getvals():
    print("Submitting form")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), paymentmodevalue.get(), foodservicevalue.get()}" )

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")



root.geometry("644x344")
# heading
Label(root, text="Welcome to RPS TRAVELS", font="comicsans,s 13 bold", pady=15).grid(row=0, column=3)

# text for form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
paymentmode = Label(root, text="Payment Mode")

# pack text for form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
paymentmode.grid(row=4, column=2)

# tkinter variables for form
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


# title
root.title("RPS TRAVELS")

# making entries
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# packing entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3 , column=3)
paymentmodeentry.grid(row=4 , column=3)

# adding checkbox and packing it
foodservice = Checkbutton(text="Want to prebook your meals", variable= foodservicevalue)
foodservice.grid(row=6, column=3)

# button for packing it and assigning a command
Button(text="Submit it to us", command=getvals).grid(row=7, column=3)




root.mainloop()