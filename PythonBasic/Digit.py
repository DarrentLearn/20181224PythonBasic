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
    '依n所代表的ASCII code，查詢字型後，顯示在7段顯示器上'
    nv = FontDigit[n]
    i = 0
    for p in PinSenvenLed:
        IO.output(p,nv[i])
        i += 1

def buttonDigits_Click(n):
    '將0~9的數字轉為ASCII code，顯示之。'
    print(n, "按下了")
    ShowDigit(n+48)

def SetDigitButton(frame, buttonText):
    '設定數字按紐。在frame內新增一個按紐，按鈕上的文字為buttonText。'
    button = Button(
        frame,
        text=buttonText,
        font=("Helvetica", 30),
        bg="Blue",
        command=lambda: buttonDigits_Click(buttonText)
    )
    button.pack(side=LEFT, padx=3, pady=3)

#對應到ASCII code的7段顯示器a~h的字型，但小數點固定為0
FontDigit = {
    32:(0, 0, 0, 0, 0, 0, 0, 0),    #空
    48 :(1, 1, 1, 1, 1, 1, 0, 0),   #0
    49 :(0, 1, 1, 0, 0, 0, 0, 0),   #1
    50 :(1, 1, 0, 1, 1, 0, 1, 0),   #2
    51 :(1, 1, 1, 1, 0, 0, 1, 0),   #3
    52 :(0, 1, 1, 0, 0, 1, 1, 0),   #4
    53 :(1, 0, 1, 1, 0, 1, 1, 0),   #5
    54 :(1, 0, 1, 1, 1, 1, 1, 0),   #6
    55 :(1, 1, 1, 0, 0, 1, 0, 0),   #7
    56 :(1, 1, 1, 1, 1, 1, 1, 0),   #8
    57 :(1, 1, 1, 0, 0, 1, 1, 0),   #9
    }

PinSenvenLed = (17,4,23,24,25,27,22,18) #7段顯示器由a~h，共8隻腳的腳位
for x in PinSenvenLed:  #逐一取出每一隻接於7段顯示器的接腳
    IO.setup(x,IO.OUT)  #設定為輸出腳
ShowDigit(32)           #顯示空白
