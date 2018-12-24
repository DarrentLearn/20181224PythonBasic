# RelayRGB7segDisplay.py
import RPi.GPIO as IO
from tkinter import *

from Relay import *
from ColorLED import *
from Digit import *

IO.setwarnings(False)
IO.setmode(IO.BCM)

if __name__ == '__main__':
    form = Tk()
    form.title('Basic control')
    form.geometry("800x600")
    form.option_add("*Button.Background","#004A9B")
    form.option_add("*Button.Foreground","white")
    formLayout_Relay(form)
    formLayout_ColorLED(form)
    formLayout_Digit(form)
    form.mainloop()