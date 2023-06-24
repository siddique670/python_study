from tkinter import messagebox
from tkinter import *

# pip install pillow

import PIL.ImageTk
import PIL.Image


class Demo:
    def __init__(self):
        self.screen = Tk()

        self.screenWidth = self.screen.winfo_screenwidth()
        self.screenHeight = self.screen.winfo_screenheight()

        # print(self.screenWidth, self.screenHeight)
        # self.screen.geometry(f"{self.screenWidth}x{self.screenHeight}")

        self.screen.geometry("1920x1080")
        self.screen.title("Demo")
        self.screen.resizable(False, False)
        self.screen.attributes('-alpha', 0.9)
        self.screen.iconbitmap("icon.ico")
        self.screen.protocol("WM_DELETE_WINDOW", self.closeScreen)

        self.backgroundImage = PIL.Image.open(r"background.jpg")
        self.backgroundImage = self.backgroundImage.resize((1920, 1080))
        self.backgroundImage = PIL.ImageTk.PhotoImage(self.backgroundImage)

        self.backgroundLabel = Label(self.screen, image=self.backgroundImage)
        self.backgroundLabel.pack()

        self.screen.mainloop()

    def closeScreen(self):
        if messagebox.askyesnocancel("Close", "Do you want to close?"):
            self.screen.destroy()


if __name__ == '__main__':
    demo = Demo()
