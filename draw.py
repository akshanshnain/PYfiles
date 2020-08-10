import pyautogui

d = 50

while d > 0:
  pyautogui.drag(d, 0, duration = 0.5)
  d -= 5
  pyautogui.drag(0, d, duration = 0.5)
  pyautogui.drag(-d, 0, duration = 0.5)
  d -= 5
  pyautogui.drag(0, -d, duration = 0.5)