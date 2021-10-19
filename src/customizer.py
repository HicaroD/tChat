import colorama
from colorama import Fore
import random

class Customizer:
    def __init__(self):
        colorama.init()

    def select_randomly(self, options : list):
        return random.choice(options)

    def select_color_for_text(self):
        """Select any color from colorama.Fore"""
        colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.MAGENTA, Fore.YELLOW,
                  Fore.CYAN, Fore.WHITE, Fore.BLUE]
        return self.select_randomly(colors)
