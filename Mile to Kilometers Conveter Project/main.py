from tkinter import *

windows=Tk()
def calculate():
    # return  int *= 1.60934
    # print(my_entery.get())
    entry=1
    if my_entery.get() == '':
        entry=1
    else:
        entry=int(my_entery.get())
    my_label_km.config(text=(entry*1.60934))
windows.title("Mile to Kilometer Converter")
windows.minsize(width=300,height=100)
windows.config(padx=20,pady=20)
my_label=Label(text="Is equal to ")
my_label.grid(row=4,column=1)
# labl_temp=Label()
# labl_temp.grid(row=0,column=0)
my_entery=Entry(width=20)
my_entery.grid(row=3,column=2)
mile_label=Label(text="Mile")
mile_label.grid(row=3,column=3)
my_label_km=Label(text=" kil ")
my_label_km.grid(row=4,column=2)

my_label_km1=Label(text="KM")
my_label_km1.grid(row=4,column=3)

my_buttom=Button(text="Calculate",width=9,height=2,command=calculate)
my_buttom.grid(row=5,column=2)

windows.mainloop()


