import pyautogui as p

# p.moveTo(41, 234, duration=1)
# p.click(41, 234)

p.hotkey('Win','r')
p.sleep(1)
p.typewrite('Notepad')
p.sleep(2)
p.press('enter')
p.sleep(2)
p.typewrite('Oi!!! eu sou um bot!!')
p.sleep(2)
valor = p.getActiveWindow()
valor.close()
p.press('right')
p.sleep(2)
p.press('enter')

# p.sleep(2)
# print(p.position())