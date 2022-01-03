import random


class Customizer:
    RESET_ANSI_CODE = "\u001b[0m"
    AMOUNT_OF_COLOR_POSSIBILITIES = 255

    def select_random_color_id(self):
        return random.randint(0, Customizer.AMOUNT_OF_COLOR_POSSIBILITIES)

    def select_color_for_text(self):
        random_color_id = self.select_random_color_id()
        color = f"\033[38;5;{random_color_id}m"
        return color
