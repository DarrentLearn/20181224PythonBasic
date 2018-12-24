import RPi.GPIO as IO
from tkinter import *

def formLayout_ColorLED(form):
    'Layout form Color LED control'
    frameColorLED = Frame(form, borderwidth=1, relief=GROOVE)
    label1 = Label(frameColorLED, text="COLOR LED 控制:",font=("Helvetica", 20))    #說明文字
    label1.pack(side=LEFT,padx=3,pady=3)
    buttonsColorLeds = ("Red","Green","Blue")   #定義LED接腳名稱
    for buttonColor in buttonsColorLeds:        #新增三個不同顏色的按紐
        SetColorLedButton(frameColorLED,buttonColor)
    frameColorLED.pack(padx=10,pady=10, fill=X)
    
def SetColorLedButton(form,color):
    '設定操控彩色LED的按鈕。在frame內新增一個按紐，按鈕上的文字為color'
    button = Button(
        form,
        text=color,
        font=("Helvetica", 20),
        bg=color,
        padx=40,
        pady=20,
        command=lambda: buttonColorLed_Click(color) #按下時，將color傳送到事件處理式
    )
    button.pack(side=LEFT, padx=3, pady=3)

def buttonColorLed_Click(color):
    '按紐事件處理式。將指定的顏色亮/滅交替。'
    colorPin=dictColorLed.get(color)    #按下的是哪個顏色的按紐
    #print("color pin:",colorPin)
    setValue = not IO.input(colorPin)   #取按紐對應的LED原來的狀態，將之反向
    if setValue == 1:
        setText = "點亮"
    else:
        setText = "熄滅"
    print(setText, color, end=". ")     #顯示亮/滅動作、顏色，只加句號不換行
    IO.output(colorPin, setValue)
    for i in ColorLed:
        print(i[0],IO.input(i[1]), end=", ")    #顯示各個顏色的值，只加逗號不換行
    print("")                           #換行

PinLedRed = 16      #LED紅色腳
PinLedGreen = 20    #LED綠色腳
PinLedBlue = 21     #LED藍色腳
ColorLed = [["Red",PinLedRed],["Green",PinLedGreen],["Blue",PinLedBlue]]    #LED顏色與接腳對應
dictColorLed=dict(ColorLed) 
for cl in ColorLed:
    #print(cl)
    IO.setup(cl[1],IO.OUT)  #逐一設定為輸出
