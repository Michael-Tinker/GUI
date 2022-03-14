import tkinter
import tkinter.messagebox

class KiloConverter:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("150x180")
        self.main_window.title("Label Demo")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame,text="Enter a distance in Kilometers")   
        self.kilo_entry = tkinter.Entry(self.top_frame,width=10)
        self.convert_button = tkinter.Button(self.button_frame,text="Convert!",command=self.convert)
        self.quit_button = tkinter.Button(self.button_frame,text="Quit",command=self.main_window.destroy)

        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")
        self.prompt_label.pack(side="top")
        self.quit_button.pack(side="left")
        self.mybutton.pack(side="right")       
        self.convert_button.pack(side="bottom")
        self.top_frame.pack(side="top")
        self.button_frame.pack(side="bottom")
        self.bottom_frame.pack(side="bottom")

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round((kilo*0.6214),2)

        tkinter.messagebox.showinfo("Results", str(kilo) + " km is equal to " + str(miles) + " miles")


km_mi = KiloConverter()

print("moving on...")

