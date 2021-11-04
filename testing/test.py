import tkcap
from tkinter import *
from tkinter.tix import *
from tkinter.font import Font
from tkinter import messagebox


class Test:
    def __init__(self):
        self.master = Tk()
        self.master.config(bg='black')
        self.master.title('tkcap - TEST')

        self.title_image = PhotoImage(file='cover.png')
        self.title = Label(self.master, image=self.title_image, bd=0, bg='black')
        self.title.pack(fill='both', expand=True)

        self.button = Button(self.master, text='CAPTURE', bd=1, fg='white', bg='black', activeforeground='grey', activebackground='black', cursor='hand2', font=Font(size=14), relief=GROOVE, command=self.capture_screenshot)
        self.button.pack(fill='x', side='bottom')

        self.button.bind('<Enter>', lambda e: self.button.config(fg='grey'))
        self.button.bind('<Leave>', lambda e: self.button.config(fg='white'))

        self.master.after(0, self.initial_position)
        self.master.bind('<Control-g>', lambda e: self.capture_screenshot())

        self.master.mainloop()

    def initial_position(self):
        '''Set self.master width and width. And set the self.master to center of the screen'''

        self.master.withdraw()
        self.master.update()
        self.master.minsize(300, 137)

        width, height = self.master.winfo_width() + 100, self.master.winfo_height() + 10
        screen_width, screen_height = self.master.winfo_screenwidth(), self.master.winfo_screenheight()

        self.master.geometry(f'{width}x{height}+{screen_width // 2 - width // 2}+{screen_height // 2 - height // 2}')
        self.master.deiconify()

    def capture_screenshot(self):
        '''Command for CAPTURE self.button or when user presses Control + g'''

        cap = tkcap.CAP(self.master)
        cap.capture('test.png', overwrite=True)


if __name__ == '__main__':
    Test()
