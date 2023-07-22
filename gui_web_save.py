#import pyautogui as pgui
#import time
##　マウスの位置を押したい場所に移動して、プログラム実行すると、座標が得られる
#pgui.position()
import pyautogui as pgui
import time
import pandas as pd
months=[]
days=[]
year='2022'
CsvFile=r"C:/sample.csv"
df=pd.read_csv(CsvFile, encoding='shift-jis', header=0, engine='python')
months=list(df['month'])
days=list(df['day'])
for month, day in zip(months, days):
    month=str(month)
    day=str(day)
    filename=year+'_'+month+'_'+day+'.html'
    pgui.click(x=1348, y=468, duration=1)
    time.sleep(10)
    pgui.hotkey('ctrl','s')
    time.sleep(0.8)
    pgui.write(filename, 0.3)
    time.sleep(0.5)
    pgui.hotkey('enter')
    time.sleep(5)