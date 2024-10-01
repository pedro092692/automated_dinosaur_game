from typing import Tuple

import pyautogui
import time

class Bot:

    def __init__(self):
        self.gui = pyautogui

    def locate_dinosaur(self):
        dino_location = self.gui.locateOnScreen('assets/dino.jpg', confidence=0.9)
        return dino_location



    def take_screenshot(self, dino_location: ()):
        """
        this function take a snapshot of the screen based on the dino position set it based on your
        screen resolution this was configured base 1080 X 1920 screen.
        dino_location is the location of the dino
        """
        img = self.gui.screenshot(region=(int(dino_location[0] + 80) ,int(dino_location[1] + 24), 80, 35))
        return img


    def check_collision(self, img):
        """
        check if there is an obstacle and it if true send jump command
        :param img: image of the game
        """
        for x in range(0 , img.size[0]):
            for y in range(0, img.size[1]):
                color = img.getpixel((x, y))
                if color == (172, 172, 172) or color == (0, 0, 0):
                    print('jump')
                    self.gui.press('space')
                    return