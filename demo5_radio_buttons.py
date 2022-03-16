import tkinter
import tkinter.messagebox

class RadioButton:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("450x700")
        self.main_window.title("Radio Button Demo")

        self.radio_var = tkinter.IntVar()

        #set intvar object to 1
        self.radio_var.set(10)

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        self.rb1 = tkinter.Radiobutton(self.top_frame, text="Option1", variable=self.radio_var, value=10)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text="Option2", variable=self.radio_var, value=20)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text="Option3", variable=self.radio_var, value=30)

        self.ok_button = tkinter.Button(self.bottom_frame,text="OK!",command=self.show_choice)
        self.reset_button = tkinter.Button(self.bottom_frame,text="Reset",command=self.rb1.select)
        self.quit_button = tkinter.Button(self.bottom_frame,text="Quit",command=self.main_window.destroy)

        #Set the default selection to the second radio button
        self.rb2.select()

        #Pack radio buttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        #Pack the buttons
        self.ok_button.pack(side="left")
        self.reset_button.pack(side="left")
        self.quit_button.pack(side="left")
        #Pack the frames
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="bottom")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("Selection", "you have selected option" + str(self.radio_var.get()))

guis = RadioButton()

print("moving on...")