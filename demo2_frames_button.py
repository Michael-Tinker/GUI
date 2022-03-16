import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("150x180")
        self.main_window.title("Label Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame,text="John")
        self.label2 = tkinter.Label(self.top_frame,text="Jill")
        self.label3 = tkinter.Label(self.top_frame,text="James")

        self.label4 = tkinter.Label(self.bottom_frame,text="Jack")
        self.label5 = tkinter.Label(self.bottom_frame,text="Jim")
        self.label6 = tkinter.Label(self.bottom_frame,text="Jerry")
        

        self.mybutton = tkinter.Button(self.button_frame,text="Click Me!",command=self.do_something)

        self.quit_button = tkinter.Button(self.button_frame,text="Quit",command=self.main_window.destroy)


        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")

        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")

        self.quit_button.pack(side="left")
        self.mybutton.pack(side="right")       
        
        self.top_frame.pack(side="top")
        self.button_frame.pack(side="bottom")
        self.bottom_frame.pack(side="bottom")

        



        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo("Response","Thanks for clicking the button")



my_gui = MyGUI()

print("moving on...")

