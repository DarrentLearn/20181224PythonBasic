import RPi.GPIO as IO
from tkinter import *

def formLayout_Relay(form):
    'Layout form relay control'    
    frameRelay = Frame(form, borderwidth=1, relief=GROOVE)
    label1 = Label(frameRelay, text="Relay 控制:",font=("Helvetica", 20))   #說明文字
    label1.pack(side=LEFT,padx=3,pady=3)
    
    #新增ON按紐
    buttonOn = Button(
        frameRelay,
        text="ON",
        font=("Helvetica", 20),
        bg="GREEN",
        padx=40,
        pady=20,
        command=lambda: buttonRelay_Click(1) #按下時，傳送1到事件處理式
        )
    buttonOn.pack(side=LEFT, padx=3,pady=3)

    #新增OFF按紐
    buttonOff = Button(
        frameRelay,
        text="OFF",
        font=("Helvetica", 20),
        bg="RED",
        padx=40,
        pady=20,
        command=lambda: buttonRelay_Click(0) #按下時，傳送0到事件處理式
        )
    buttonOff.pack(side=LEFT, padx=3,pady=3)
    
    frameRelay.pack(padx=10,pady=10, fill=X)
    
def buttonRelay_Click(flag):
    '顯示按下了哪個按紐，並使Relay依ON/OFF動作'
    if flag == 0:
        print ("OFF 按下了")
    else:
        print ("ON 按下了")
    IO.output(PinRelay,flag)

PinRelay = 12   #定義relay接腳
IO.setup(PinRelay,IO.OUT)     #設定為輸出腳
