import random

class Customizer:
    RESET_ANSI_CODE = "\u001b[0m"

    def select_random_color_number(self):
        return random.randint(30, 37)

    def select_color_for_text(self):
        """Select any color from colorama.Fore"""
        random_color_number = self.select_random_color_number()
        color = f"\u001b[{random_color_number};1m"
        return color
