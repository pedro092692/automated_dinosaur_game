from  browser import Browser
from bot import Bot
import time

browser = Browser()
bot = Bot()

# start game and play
browser.start_game()
browser.get_canvas_coordinate()
bot.locate_dinosaur()