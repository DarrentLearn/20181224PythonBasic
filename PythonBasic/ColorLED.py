import RPi.GPIO as IO
from tkinter import *

def formLayout_ColorLED(form):
    'Layout form Color LED control'
    frameColorLED = Frame(form, borderwidth=1, relief=GROOVE)

    label1 = Label(frameColorLED, text="COLOR LED 控制:",font=("Helvetica", 20))
    label1.pack(side=LEFT,padx=3,pady=3)

    buttonsColorLeds = ("Red","Green","Blue")
    for buttonColor in buttonsColorLeds:
        SetColorLedButton(frameColorLED,buttonColor)
    
    frameColorLED.pack(padx=10,pady=10, fill=X)
    
def SetColorLedButton(form,color):
    button = Button(
        form,
        text=color,
        font=("Helvetica", 20),
        bg=color,
        padx=40,
        pady=20,
        command=lambda: buttonColorLed_Click(color)
    )
    button.pack(side=LEFT, padx=3, pady=3)

def buttonColorLed_Click(color):
    colorPin=dictColorLed.get(color)
    #print("color pin:",colorPin)
    setValue = not IO.input(colorPin)
    if setValue == 1:
        setText = "點亮"
    else:
        setText = "熄滅"
    print(setText, color, end=". ")
    IO.output(colorPin, setValue)
    for i in ColorLed:
        print(i[0],IO.input(i[1]), end=", ")
    print("")

PinLedRed = 16
PinLedGreen = 20
PinLedBlue = 21
ColorLed = [["Red",PinLedRed],["Green",PinLedGreen],["Blue",PinLedBlue]]
dictColorLed=dict(ColorLed)
for cl in ColorLed:
    #print(cl)
    IO.setup(cl[1],IO.OUT)
