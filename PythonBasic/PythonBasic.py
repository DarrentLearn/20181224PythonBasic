# RelayRGB7segDisplay.py
import RPi.GPIO as IO
from tkinter import *

from Relay import *     #匯入relay程式
from ColorLED import *  #匯入彩色LED程式
from Digit import *     #匯入數字按紐與7段顯示器程式

IO.setwarnings(False)
IO.setmode(IO.BCM)

if __name__ == '__main__':
    form = Tk()                                     #新建表單視窗
    form.title('Basic control')                     #表單視窗抬頭
    form.geometry("800x600")                        #表單視窗尺寸
    form.option_add("*Button.Background","#004A9B") #預設按紐背景色
    form.option_add("*Button.Foreground","white")   #預設按紐文字顏色
    formLayout_Relay(form)                          #定義relay按紐與輸出處理
    formLayout_ColorLED(form)                       #定義彩色LED按紐與輸出處理
    formLayout_Digit(form)                          #定義數字按紐與7段顯示器處理
    form.mainloop()