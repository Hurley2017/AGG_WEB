import tkinter
import os
from threading import Thread

class Launcher():
    def __init__(self):
        self.Window_Config()


        

    def Window_Config(self):
        self.root = tkinter.Tk()
        self.root.title("Attack Graph Generator")
        self.root.geometry("800*500+400+400")
        self.root.resizable(False, False)   

    def Invoke_Main(self):
        os.system("python3 main.py")

    def Launch(self):
        Thread(target=self.Invoke_Main).start()    

    def Start_Engine(self):
        self.root.mainloop()

if __name__ == "__main__":
    Instance = Launcher()
    Instance.Invoke_Main()

