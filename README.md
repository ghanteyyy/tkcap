```
   __      __
  /  |    /  |
 _$$ |_   $$ |   __   _______   ______    ______
/ $$   |  $$ |  /  | /       | /      \  /      \
$$$$$$/   $$ |_/$$/ /$$$$$$$/  $$$$$$  |/$$$$$$  |
  $$ | __ $$   $$<  $$ |       /    $$ |$$ |  $$ |
  $$ |/  |$$$$$$  \ $$ \_____ /$$$$$$$ |$$ |__$$ |
  $$  $$/ $$ | $$  |$$       |$$    $$ |$$    $$/
   $$$$/  $$/   $$/  $$$$$$$/  $$$$$$$/ $$$$$$$/
                                        $$ |
                                        $$ |
                                        $$/
```

A wrapper for tkinter window for taking its screenshot. <br>

Ghanteyyy http://github.com/ghanteyyy
MIT License

# Requirements and Tested Platforms
* Python:
  > * 3.x

* Windows (32bit/64bit):
  > * Windows 10

# Installation

tkcap is available on PyPI. You can install it through pip:

```pip install tkcap```

# Usage

```python

import tkcap

cap = tkcap.CAP(master)     # master is an instance of tkinter
cap.capture(FileName)       # Capture and Save the screenshot of the tkiner window

# If you want the x_pos, y_pos, width and height of the tkinter window.
region = cap.get_region()

# If you want to bind the key so that everytime you press that key
# captures the screenshot. Here I have binded "Control g":
# Set 'overwrite' parameter to True, to overwrite the file having same name
master.bind('<Control-g>', lambda: cap.capture(FileName))
```
