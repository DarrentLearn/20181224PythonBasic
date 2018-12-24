import RPi.GPIO as IO
from tkinter import *

def formLayout_Digit(form):
    'Layout form digitl Control'
    frameDigit = Frame(form, borderwidth=1, relief=GROOVE)

    label1 = Label(frameDigit, text="數字顯示:",font=("Helvetica", 20))
    label1.pack(side=LEFT,padx=3,pady=3)

    for i in range(10):
        SetDigitButton(frameDigit, i)
    frameDigit.pack(padx=10, pady=10, fill=X)

def ShowDigit(n):
    nv = FontDigit[n]
    i = 0
    for p in PinSenvenLed:
        IO.output(p,nv[i])
        i += 1

def buttonDigits_Click(n):
    print(n, "按下了")
    ShowDigit(n)

def SetDigitButton(frame, buttonText):
    button = Button(
        frame,
        text=buttonText,
        font=("Helvetica", 30),
        bg="Blue",
        command=lambda: buttonDigits_Click(buttonText)
    )
    button.pack(side=LEFT, padx=3, pady=3)

FontDigit = {
    0 :(1, 1, 1, 1, 1, 1, 0, 0),
    1 :(0, 1, 1, 0, 0, 0, 0, 0),
    2 :(1, 1, 0, 1, 1, 0, 1, 0),
    3 :(1, 1, 1, 1, 0, 0, 1, 0),
    4 :(0, 1, 1, 0, 0, 1, 1, 0),
    5 :(1, 0, 1, 1, 0, 1, 1, 0),
    6 :(1, 0, 1, 1, 1, 1, 1, 0),
    7 :(1, 1, 1, 0, 0, 1, 0, 0),
    8 :(1, 1, 1, 1, 1, 1, 1, 0),
    9 :(1, 1, 1, 0, 0, 1, 1, 0),
    10:(0, 0, 0, 0, 0, 0, 0, 0),
    }

PinSenvenLed = (17,4,23,24,25,27,22,18)
for x in PinSenvenLed:
    IO.setup(x,IO.OUT)
