import tkinter
import tkinter.messagebox

class GradeAverage:
    def __init__(self):
        #Main Window
        self.main_window = tkinter.Tk()

        #Window Details
        self.main_window.geometry("600x300")
        self.main_window.title("Test Average Exercise Demo")
        self.main_window.configure(bg='green')

        #Frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.average_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #Labels for test entry
        self.prompt1_label = tkinter.Label(self.test1_frame,text="Enter the score for test 1: ")   
        self.prompt2_label = tkinter.Label(self.test2_frame,text="Enter the score for test 2: ")
        self.prompt3_label = tkinter.Label(self.test3_frame,text="Enter the score for test 3: ")  


        #Entry
        self.test1_entry = tkinter.Entry(self.test1_frame,width=10)
        self.test2_entry = tkinter.Entry(self.test2_frame,width=10)
        self.test3_entry = tkinter.Entry(self.test3_frame,width=10)

        #Average Labels + Label Output
        self.avg_var = tkinter.StringVar()
        self.average_label = tkinter.Label(self.average_frame,text="Average: ")  
        self.average_output_label = tkinter.Label(self.average_frame, textvariable=self.avg_var)

        #Buttons
        self.average_button = tkinter.Button(self.button_frame,text="Average",command=self.average_scores)
        self.quit_button = tkinter.Button(self.button_frame,text="Quit",command=self.main_window.destroy)

        #Packing
        self.prompt1_label.pack(side="left")
        self.test1_entry.pack(side="right")

        self.prompt2_label.pack(side="left")
        self.test2_entry.pack(side="right")

        self.prompt3_label.pack(side="left")
        self.test3_entry.pack(side="right")

        self.average_label.pack(side="left")
        self.average_output_label.pack(side="right")


        self.average_button.pack(side="left")
        self.quit_button.pack(side="right")

        self.test1_frame.pack(side="top")
        self.test2_frame.pack(side="top")
        self.test3_frame.pack(side="top")
        self.average_frame.pack(side="top")
        self.button_frame.pack(side="top")

        #idk
        tkinter.mainloop()

    #Calculate the Average
    def average_scores(self):
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())
        finalaverage = round(((test1+test2+test3)/3),2)

        self.avg_var.set(finalaverage)

        #tkinter.messagebox.showinfo("Average:", str(finalaverage))

#call the class thingy
gui = GradeAverage()

print("moving on...")