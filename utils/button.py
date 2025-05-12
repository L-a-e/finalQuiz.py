from .settings import * 

class Button:
    def __init__(self, x, y, width, height,color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        if self.text:
            pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 2)


    def clicked(self, pos):
        pass