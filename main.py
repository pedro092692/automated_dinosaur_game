from  browser import Browser
from bot import Bot
import time

browser = Browser()
bot = Bot()

# start game and play
browser.start_game()
# time for start game
time.sleep(4)
# locate dino on the screen
dino_position = bot.locate_dinosaur()
while True:
    # take a snapshot of impact point
    img = bot.take_screenshot(dino_location=(dino_position.left, dino_position.top))
    # check if there is an obstacle
    bot.check_collision(img=img)
    time.sleep(0.01)