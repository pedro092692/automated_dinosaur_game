import pyautogui


class Bot:

    def __init__(self):
        self.gui = pyautogui

    def locate_dinosaur(self):
        dino_location = self.gui.locateOnScreen('assets/dino.jpg', confidence=0.9)
        print(dino_location)
        pix = self.gui.pixel(674, 250)
        self.gui.screenshot('test.png', region=(640,160, 640, 160))