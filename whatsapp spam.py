import pyautogui as auto
from time import sleep
import webbrowser as wb

wb.open("https://web.whatsapp.com/")

sleep(10)

for i in range(100):
    auto.write("Hello Guys. Let's have fun!!")
    auto.press("enter")

# After whatsapp web opens select the chat you want to spam