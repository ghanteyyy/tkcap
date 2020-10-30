'''
tkcap

A wrapper for tkinter window for taking its screenshot.
By ghanteyyy http://github.com/ghanteyyy
MIT License

Usage:
    import tkcap

    cap = tkcap.CAP(master)    # master is an instance of tkinter
    cap.capture(FileName)       # Capture and Save the screenshot of the tkiner window

    # If you want the x_pos, y_pos, width and height of the tkinter window.
    region = cap.get_region()

    # If you want to bind the key so that everytime you press that key
    # captures the screenshot. Here I have binded "Control g":
    # Set 'overwrite' parameter to True, to overwrite the file having same name
    master.bind('<Control-g>', lambda: cap.capture(FileName))
'''

__all__ = ['CAP']
__version__ = '0.0.1'
__author__ = 'ghanteyyy'

import os
import sys
import winsound
import subprocess
import collections
import tkinter as tk
import tkinter.tix as tix

from . import exceptions

if sys.version_info.major < 3:
    raise exceptions.TkCapException('tkcap supports Python 3+')

try:
    import pyautogui

except ModuleNotFoundError:
    raise exceptions.TkCapException('tkcap is unable to import pyautogui. Please install pyautogui to use tkcap')


Region = collections.namedtuple('Region', 'x y width height')


class CAP:
    def __init__(self, master):
        if isinstance(master, (tk.Tk, tk.Toplevel, tix.Tk, tix.Toplevel)):
            self.master = master
            self.wav_path = os.path.join(os.path.dirname(__file__), 'data', 'shutter.wav')
            self.VALID_EXTENSION = ['tif', 'tiff', 'jpg', 'png', 'jpeg', 'jpe', 'jfif', 'bmp', 'dib', 'gif']

        else:
            raise exceptions.TkCapException('master parameter was expected to be the instance of tkinter')

    def get_region(self):
        '''Gets x-coordinate, y-coordinate, width and height of the tkinter window'''

        self.master.update()

        x_pos, y_pos = self.master.winfo_x() + 8, self.master.winfo_y() + 2
        width, height = self.master.winfo_width(), self.master.winfo_height() + 29

        return Region(x_pos, y_pos, width, height)

    def capture(self, imageFilename, overwrite=False):
        '''Capture and save screenshot of the tkinter window'''

        path = os.path.abspath(os.path.join('.', imageFilename))
        head, tail = os.path.split(path)
        extension = tail.split('.')[-1]

        if not os.path.exists(head):
            raise exceptions.PathNotFoundError(f'The system cannot find path: {head}')

        elif extension not in self.VALID_EXTENSION:
            if '.' in tail:
                extension = '.' + extension

            else:  # If extension is not provided by the user.
                extension = ''

            raise exceptions.ExtensionError(f'unknown file extension: {extension}')

        elif os.path.exists(path) and overwrite is False:
            raise exceptions.ImageNameExistsError(f'Cannot store image having same name: {tail}')

        if overwrite:
            os.remove(path)

        winsound.PlaySound(self.wav_path, winsound.SND_ASYNC)

        pyautogui.screenshot(path, region=self.get_region())

        self.master.after(1100, lambda: subprocess.run([os.path.join(os.getenv('WINDIR'), 'explorer.exe'), '/select,', os.path.normpath(path)]))
