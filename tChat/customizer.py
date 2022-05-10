import random


class Customizer:
    RESET_ANSI_CODE = "\u001b[0m"

    def select_random_color_id(self):
        return random.randint(80, 231)

    def select_color_for_text(self):
        random_color_id = self.select_random_color_id()
        black_background_color = "\u001b[40;1m"
        color = f"\033[38;5;{random_color_id}m"
        return color
