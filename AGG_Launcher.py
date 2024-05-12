import os
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import time
from threading import Thread

class Console():
    def __init__(self):
        self.Main = Tk()
        self.Window_Config()
        self.Memory()
        self.load_Contents()

    #####################################################
    ################## Actual Console ###################
    #####################################################

    def Excuse_Buffer(self, duration):
        time.sleep(duration)
    
    def PTrace(self, T):
        return "\t"+"\n\t".join([line for line in T.split('\n')])

    def Window_Config(self):
        self.Main.wm_title('Debugging Console X Launcher for Attack Graph Generator')
        width = 850
        height = 545
        screen_width = self.Main.winfo_screenwidth()
        screen_height = self.Main.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.Main.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.Main.grid_columnconfigure(1,minsize=70,weight=1)
        self.Main.configure(bg='white')
        self.Main.resizable(False, False)
    
    def load_Contents(self):
        self.load_CFX_HEADER()
        self.load_BUTTON_FRAME()
        self.load_Console_Frame()

    def load_CFX_HEADER(self):
        self.Title = Label(self.Main, text='Attack Graph Generator', height=2, font=('Ariel', 25, 'bold'), fg='white', bg='blue4')
        self.Title.grid(row=0, column=0, padx=10, pady=5, columnspan=10, sticky='ew')

    def load_BUTTON_FRAME(self):
        Shift = 9
        self.Button_Frame = Frame(self.Main, width=650, height=100, background='lightgray', highlightbackground="black", highlightthickness=1)
        self.Button_Frame.grid(row=1, column=0, padx=10, pady=5, columnspan=10, sticky='ew')
        self.Start_Button = Button(self.Button_Frame, text='Start Engine', width=15, height=1, command=self.Start_Process, font=('courier', 20, "bold"), fg='white', bg='green')  
        self.Start_Button.place(x=Shift+10, y=20)
        self.Stop_Button = Button(self.Button_Frame, text='Stop Engine', width=15, height=1, command=self.Start_Process, font=('courier', 20, "bold"), fg='white', bg='red4')  
        self.Stop_Button.place(x=Shift+280, y=20)
        self.Github_Button = Button(self.Button_Frame, text=' GitHub', width=15, height=1, command=self.Start_Process, font=('courier', 20, "bold"), fg='white', bg='black')
        # 
        self.Github_Button.place(x=Shift+550, y=20)
        self.Git_logo = PhotoImage(file='github.png')
        self.Git_logo = self.Git_logo.subsample(15)
        self.Git = Label(self.Button_Frame, image=self.Git_logo)
        self.Git.place(x=Shift+560, y=30)

    
    def load_Console_Frame(self):
        self.Console_Frame = Frame(self.Main, width=650, height=327, background='lightgray', highlightbackground="black", highlightthickness=1)
        self.Console_Frame.grid(row=2, column=0, padx=10, pady=5, columnspan=10, sticky='ew')

        self.Console_Out = ScrolledText(self.Console_Frame, width=200,  height= 20, )
        self.Console_Out.pack(fill=BOTH, side=LEFT, expand=True)

        self.Curr_Data = '''\tHello there.
        This is a standard console.
        Your process states, outputs and error tracebacks will appear here.
        Do to panic. This Window will keep you updated.'''
        
        self.Update_Console(self.Curr_Data)

    def Update_Console(self, WData):
        self.Curr_Data += WData
        WData += '\n\t----------------------------------------------------------------------\n'
        self.Console_Out.insert('end', WData)

    def Show_Status(self, Process):
        self.Update_Console('\n\t*Status enquiry called by user for '+Process+' process.*')
        if Process in self.Processed:
            messagebox.showinfo('Status', Process+' is completed successfully. Check Results.')
            return
        if Process in self.ToBeProcessed:
            messagebox.showinfo('Status', Process+' is yet not started. Please wait.')
            return
        if self.Curr_Status == Process:
            messagebox.showwarning('Status', Process+' is currently being executed. Please deal with Excel/System dialogues outside the tool.')
            return
        messagebox.showerror('Status', Process+' not defined in Memory.')
        
    
    def Memory(self):
        self.Curr_Status = None
        self.Processed = []
        self.ToBeProcessed = ['Excel to PPT', 'Control/Validation']

    def Start_Engine(self):
        self.Main.mainloop()
    
    #####################################################
    ################# Actual Functions ##################
    #####################################################

    def Start_Process(self):
        try:
            self.Excuse_Buffer(5)
        except Exception as e:
            self.Update_Console('\tError Test : '+str(e))

if __name__ == "__main__":
    Instance = Console()
    Instance.Start_Engine()