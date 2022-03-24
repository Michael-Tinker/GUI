#Design a creative UI using Python's tkinter module to calculate the total cost of a pizza. The UI should have (at least) each widget that was covered in class:

    #Frames
    #Labels
    #input box
    #buttons
    #radio buttons
    #check boxes

#You can use check boxes for for selecting toppings (each with a different cost), radio buttons for the type of crust selected 
# (each with a different cost), buttons for calculation and quit. The input box can be used to record the name of the person placing the order. 
# Use a message box to display the total cost of the pizza along with the name of the person placing the order.

#Make sure your design is well laid out and intuitive to the user. Take account of spacing and packing so that everything is 
# properly aligned and professional looking. Be creative with font, color, size, etc.



import tkinter
import tkinter.messagebox

class PizzaTime:
    def __init__(self):
#Main Window
        self.main_window = tkinter.Tk()

#Window Details
        #self.main_window.geometry("600x300")
        self.main_window.title("Pizza Planet Ordering Application")
        self.main_window.configure(bg='blue')

#Frames
        self.title_frame = tkinter.Frame(self.main_window)
        self.crust_frame = tkinter.Frame(self.main_window)
        self.toppings_frame = tkinter.Frame(self.main_window)
        self.calculation_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.customer_frame = tkinter.Frame(self.main_window)
        self.spacer1_frame = tkinter.Frame(self.main_window)
        self.spacer2_frame = tkinter.Frame(self.main_window)
        self.spacer3_frame = tkinter.Frame(self.main_window)
        self.spacer4_frame = tkinter.Frame(self.main_window)


#Title Header
        self.title_label = tkinter.Label(self.title_frame,text="Pizza Planet Ordering System")
        self.subtitle_label = tkinter.Label(self.title_frame,text='''"Our Pizza is out of this world!"''')

#Spacer
        self.spacer1_label = tkinter.Label(self.spacer1_frame,text="")

#Crust

        #Label
        self.crust_label = tkinter.Label(self.crust_frame,text="Select The Crust")

        #Instance
        self.radio_var = tkinter.IntVar()

        #set intvar object to 1
        self.radio_var.set(8)

        #Radio Buttons for Crust
        self.rb1 = tkinter.Radiobutton(self.crust_frame, text="Regular Crust ($8.00)", variable=self.radio_var, value=8)
        self.rb2 = tkinter.Radiobutton(self.crust_frame, text="Thin Crust    ($7.00)", variable=self.radio_var, value=7)
        self.rb3 = tkinter.Radiobutton(self.crust_frame, text="Stuffed Crust ($12.00)", variable=self.radio_var, value=12)

        #Set the default selection
        self.rb1.select()

#Spacer
        self.spacer2_label = tkinter.Label(self.spacer2_frame,text="")

#Toppings - Checkboxes

        #Label
        self.toppings_label = tkinter.Label(self.toppings_frame,text="Select The Toppings")

        #Create three intvar objects to use with the checkbuttons.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        #Set the intvar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        #Checkboxes
        self.cb1 = tkinter.Checkbutton(self.toppings_frame, text="Peperoni ($1.00)", variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.toppings_frame, text="Black Olives ($0.75)", variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.toppings_frame, text="Italian Sausage ($1.25)", variable=self.cb_var3)

#Spacer
        self.spacer3_label = tkinter.Label(self.spacer3_frame,text="")

#Buttons

        self.mybutton = tkinter.Button(self.button_frame,text="Calculate Cost",command=self.calculate_cost)
        self.quit_button = tkinter.Button(self.button_frame,text="Quit",command=self.main_window.destroy)

#Spacer
        self.spacer4_label = tkinter.Label(self.spacer4_frame,text="")

#Customer Details - Input Boxes
        self.entry_label = tkinter.Label(self.customer_frame,text="Customer Name: ")
        self.name_entry = tkinter.Entry(self.customer_frame,width=20)

#Order Confirmation - Message Box with Name of Person Placing Order

#Packing

        #Pack the heading labels
        self.title_label.pack(side="top")
        self.subtitle_label.pack(side="top")

        #Packing spacers
        self.spacer1_label.pack()
        self.spacer2_label.pack()
        self.spacer3_label.pack()
        self.spacer4_label.pack()

        #Pack the Checkboxes and Label for Toppings
        self.toppings_label.pack()
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        #Pack radio buttons
        self.crust_label.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #Pack the Calculation and Quit Buttons
        self.mybutton.pack(side="left")
        self.quit_button.pack(side="right")

        #Pack the customer entry label and field
        self.entry_label.pack(side="left")
        self.name_entry.pack(side="right")

        #Pack the frames
        self.title_frame.pack(side="top")
        self.spacer1_frame.pack(side="top")
        self.crust_frame.pack(side="top")
        self.spacer2_frame.pack(side="top")
        self.toppings_frame.pack(side="top")
        self.spacer3_frame.pack(side="top")
        self.customer_frame.pack(side="top")
        self.spacer4_frame.pack(side="top")
        self.button_frame.pack(side="top")

#idk
        tkinter.mainloop()

#Calculations
    def calculate_cost(self):
        self.message = "Pizza Order Summary For Customer: "
        
        #if self.name_entry.get() != "":
        self.message += self.name_entry.get() + "\n"

        self.message += "Your pizza will cost: "
        
        pizza_cost = self.radio_var.get()

        if self.cb_var1.get() == 1:
            #self.message += "1\n"
            pizza_cost += 1
        if self.cb_var2.get() == 1:
            #self.message += "2\n"
            pizza_cost += .75
        if self.cb_var3.get() == 1:
            #self.message += "3\n"
            pizza_cost += 1.25

        self.message += "$" + str(pizza_cost)
        tkinter.messagebox.showinfo("Total Cost",self.message)

#call the class thingy
gui = PizzaTime()

print("moving on...")