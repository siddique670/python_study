from tkinter import messagebox
from tkinter import *

# pip install pillow

import PIL.ImageTk
import PIL.Image


class MusicPlayer:
    def __init__(self):
        self.screen = Tk()

        self.screenWidth = self.screen.winfo_screenwidth()
        self.screenHeight = self.screen.winfo_screenheight()

        # print(self.screenWidth, self.screenHeight)
        # self.screen.geometry(f"{self.screenWidth}x{self.screenHeight}")

        self.screen.geometry("1920x1080")
        self.screen.title("Music Player")
        self.screen.resizable(False, False)
        self.screen.attributes('-alpha', 0.9)
        self.screen.iconbitmap("icon.ico")
        self.screen.protocol("WM_DELETE_WINDOW", self.closeScreen)

        self.backgroundImage = PIL.Image.open(r"background.jpg")
        self.backgroundImage = self.backgroundImage.resize((1920, 1080))
        self.backgroundImage = PIL.ImageTk.PhotoImage(self.backgroundImage)

        self.songImage = PIL.Image.open(r"song.jpg")
        self.songImage = self.songImage.resize((450, 200))
        self.songImage = PIL.ImageTk.PhotoImage(self.songImage)

        self.backgroundLabel = Label(self.screen, image=self.backgroundImage)
        self.backgroundLabel.pack()

        self.titleLabel = Label(self.backgroundLabel, text="MUSIC PLAYER", font=("Olive Village", 30, "bold"), bg="#fac304")
        self.titleLabel.place(x=0, y=0, relwidth=1)

        self.setupPlayer()

        self.screen.mainloop()

    def setupPlayer(self):
        self.playerFrame = Frame(self.backgroundLabel, width=450, height=550, bg="#9396a7", bd=2, relief="groove")
        self.playerFrame.place(x=750, y=250)

        self.songImageLabel = Label(self.playerFrame, image=self.songImage)
        self.songImageLabel.place(x=0, y=0)

        self.songTitleLabel = Label(self.playerFrame, text="Ab Na Phir Se", font=("fira code", 18, "bold"), fg="white", bg="#9396a7")
        self.songTitleLabel.place(x=0, y=220, relwidth=1)

        self.playButton = Button(self.playerFrame, text="Play", width=24, font=("fira code", 16, "bold"), bg="#fac304")
        self.playButton.place(x=50, y=290)

        self.pauseButton = Button(self.playerFrame, text="Pause", width=24, font=("fira code", 16, "bold"), bg="#fac304")
        self.pauseButton.place(x=50, y=360)

        self.resumeButton = Button(self.playerFrame, text="Resume", width=24, font=("fira code", 16, "bold"), bg="#fac304")
        self.resumeButton.place(x=50, y=430)

    def closeScreen(self):
        if messagebox.askyesnocancel("Close", "Do you want to close?"):
            self.screen.destroy()


if __name__ == '__main__':
    player = MusicPlayer()
