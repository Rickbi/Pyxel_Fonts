import pyxel

class Button:
    def __init__(self, pos_x, pos_y, width, height, funct = None):
        self.pos = [pos_x, pos_y]
        self.size = [width, height]
        self.hover = False
        self.press = False
        self.funct = funct
    
    def draw(self):
        color_1 = pyxel.COLOR_NAVY
        color_2 = pyxel.COLOR_GRAY
        
        if self.press:
            color_1 = pyxel.COLOR_DARK_BLUE
            color_2 = pyxel.COLOR_WHITE
        elif self.hover:
            color_1 = pyxel.COLOR_DARK_BLUE
            color_2 = pyxel.COLOR_GRAY

        pyxel.rect(*self.pos, *self.size, color_1)
        pyxel.rectb(*self.pos, *self.size, color_2)

    def handle_button_press(self):
        if self.funct and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.funct()
        
    def update(self):
        self.hover = False
        self.press = False
        # Check collition with mouse.
        if self.pos[0] <= pyxel.mouse_x < self.pos[0] + self.size[0]:
            if self.pos[1] <= pyxel.mouse_y < self.pos[1] + self.size[1]:
                self.hover = True
                # Check for left click event to give the visual press
                if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                    self.press = True                
                # Check for left click event
                self.handle_button_press()


class HoldButton(Button):
    def __init__(self, pos_x, pos_y, width, height, funct = None, hold = 10, repeat = 5):
        super().__init__(pos_x, pos_y, width, height, funct)
        self.hold = hold
        self.repeat = repeat

    def handle_button_press(self):
        if self.funct and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT, self.hold, self.repeat):
            self.funct()


class ImageButton(Button):
    def __init__(self, pos_x, pos_y,
                 img_bank, u, v, width, height,
                 funct = None, uh = -1, vh = -1, up = -1, vp = -1, alpha = 0):
        super().__init__(pos_x, pos_y, width, height, funct)
        
        self.img_bank = img_bank
        self.alpha = alpha
        
        uh = u if uh < 0 else uh
        vh = v if vh < 0 else vh
        up = u if up < 0 else up
        vp = v if vp < 0 else vp
       
        self.pos_imgs = [(u, v), (uh, vh), (up, vp)]
    
    def draw(self):
        if self.press:
            pyxel.blt(*self.pos, self.img_bank, *self.pos_imgs[2], *self.size, self.alpha)
        elif self.hover:
            pyxel.blt(*self.pos, self.img_bank, *self.pos_imgs[1], *self.size, self.alpha)
        else:
            pyxel.blt(*self.pos, self.img_bank, *self.pos_imgs[0], *self.size, self.alpha)


class ImageHoldButton(ImageButton, HoldButton):
    def __init__(self, pos_x, pos_y,
                 img_bank, u, v, width, height,
                 funct = None, uh = -1, vh = -1, up = -1, vp = -1,
                 alpha = 0, hold = 10, repeat = 5):
        super().__init__(pos_x, pos_y, img_bank, u, v, width, height, funct, uh, vh, up, vp, alpha)
        self.hold = hold
        self.repeat = repeat


class TextButton(Button):
    def __init__(self, pos_x, pos_y, text, funct = None):
        lines = [len(line) for line in text.split("\n")]
        w = pyxel.FONT_WIDTH * max(lines) + 4 - 1
        h = pyxel.FONT_HEIGHT * len(lines) + 4 - 1
        super().__init__(pos_x, pos_y, w, h, funct)
        self.text = text
        
    def draw(self):
        super().draw()
        pyxel.text(self.pos[0] + 2, self.pos[1] + 2, self.text, pyxel.COLOR_WHITE)


class TextHoldButton(TextButton, HoldButton):
    def __init__(self, pos_x, pos_y, text, funct = None,
                 hold = 10, repeat = 5):
        super().__init__(pos_x, pos_y, text, funct)
        self.hold = hold
        self.repeat = repeat
        
