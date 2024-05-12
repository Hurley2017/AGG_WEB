import os
from main import app  
import socket
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import time
from multiprocessing import Process
from threading import Thread
from random import randint
import traceback
import requests


class Console():
    def __init__(self, FServer):
        self.Alive = False
        self.Local_Host = self.get_IP()
        self.Local_Port = str(randint(1001, 9999))
        self.Main = Tk()
        self.Window_Config()
        self.load_Contents()
        self.Main_T = Thread(target=self.Main_Process)
        self.Application = FServer

    #####################################################
    ################## Actual Console ###################
    #####################################################
    def get_IP(self):
        return socket.gethostbyname(socket.gethostname())

    def Excuse_Buffer(self, duration):
        time.sleep(duration)
    
    def Main_Process(self):
        try:
            self.Alive = True
            try:
                self.Application.run(host=self.Local_Host, port=self.Local_Port)
            except RuntimeError as R:
                self.Update_Console('\tServer balabalalalalal Stopped Internally: '+str(R))
                self.Update_Console('\tIgnore Traceback...\n\t'+self.PTrace(traceback.format_exc()))  
                exit(0)  
        except Exception as e:
            self.Update_Console('\tError in Main Process: '+str(e))
            self.Update_Console('\tMain Process Failed...\n\t'+self.PTrace(traceback.format_exc()))

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
        self.Stop_Button = Button(self.Button_Frame, text='Stop Engine', width=15, height=1, command=self.Stop_Process, font=('courier', 20, "bold"), fg='white', bg='red4')  
        self.Stop_Button.place(x=Shift+280, y=20)
        self.Github_Button = Button(self.Button_Frame, text=' GitHub', width=15, height=1, command=self.Github_Process, font=('courier', 20, "bold"), fg='white', bg='black')
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

    def Start_Engine(self):
        self.Main.mainloop()
    
    #####################################################
    ################# Actual Functions ##################
    #####################################################
    def Github_Process(self):
        try:
            self.Update_Console('\tOpening Github Page...')
            os.system('start https://github.com/Hurley2017/AGG_WEB')
        except Exception as e:
            self.Update_Console('\tError Test : '+str(e))
            self.Update_Console('\tGithub Process Failed...\n\t'+self.PTrace(traceback.format_exc()))  


    def Start_Process(self):
        try:
            if self.Alive:
                self.Update_Console('\tEngine Already Running...')
                messagebox.showwarning('Server is Alive', 'Dismiss the alert to open the default browser.')
                os.system('start http://'+self.Local_Host+':'+self.Local_Port+'/')
                return
            else:
                self.Update_Console('\tStarting Engine...'+'\n\tLocal Host : '+self.Local_Host+'\n\tLocal Port : '+self.Local_Port+'\n\tDialing Engine (Check default browser)...')
                os.system('start http://'+self.Local_Host+':'+self.Local_Port+'/')
                self.Main_T.start()
        except Exception as e:
            self.Update_Console('\tError in Process : '+str(e))
            self.Update_Console('\tStarting Engine Failed...\n\t'+self.PTrace(traceback.format_exc()))  

    def Stop_Process(self):
        try:
            if not self.Alive:
                self.Update_Console('\tEngine is not running...')
                messagebox.showwarning('Error', 'Server is not alive.')
                return 
            else:
                self.Update_Console('\tStopping Engine...')
                self.Alive = False
                Response = requests.get('http://'+self.Local_Host+':'+self.Local_Port+'/shutdown')
                self.Update_Console('\t'+self.PTrace(Response.text))
                self.Main_T.join()
                self.Main_T = Thread(target=self.Main_Process)
        except Exception as e:
            self.Update_Console('\tError Test : '+str(e)) 
            self.Update_Console('\tFatal Error...\n\t'+self.PTrace(traceback.format_exc()))         

if __name__ == "__main__":
    Instance = Console(app)
    Instance.Start_Engine()